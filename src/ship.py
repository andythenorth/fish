# get the globals - however for using globals in templates, it's better for the template to use global_template.pt as a macro
import global_constants # expose all constants for easy passing to templates

from pprint import pprint

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs

import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

from ships import registered_ships

import legacy_config_handler

config = legacy_config_handler.config



class Ship(object):
    """Base class for all types of ships"""
    def __init__(self, id, **kwargs):
        self.id = id

        #setup properties for this vehicle
        self.title = kwargs.get('title', None)
        self.numeric_id = kwargs.get('numeric_id', None)
        self.custom_template = kwargs.get('custom_template', None)
        self.str_type_info = kwargs.get('str_type_info', None).upper()
        # supertype controls refits etc, so figure it out from the type
        self.supertype = global_constants.type_supertype_mapping[self.str_type_info.lower()]
        self.graphics_template = kwargs.get('graphics_template', None)
        self.intro_date = kwargs.get('intro_date', None)
        self.replacement_id = kwargs.get('replacement_id', None)
        #print self.replacement_id
        self.vehicle_life = kwargs.get('vehicle_life', None)
        self.speed = kwargs.get('speed', None)
        self.speed_unladen = self.speed * kwargs.get('speed_factor_unladen', None)
        self.buy_cost = kwargs.get('buy_cost', None)
        self.fixed_run_cost_factor = kwargs.get('fixed_run_cost_factor', None)
        self.fuel_run_cost_factor = kwargs.get('fuel_run_cost_factor', None)
        self.gross_tonnage = kwargs.get('gross_tonnage', None)
        self.capacity_pax = kwargs.get('capacity_pax', None)
        self.capacity_mail = kwargs.get('capacity_mail', None)
        self.capacity_cargo_holds = kwargs.get('capacity_cargo_holds', None)
        self.capacity_tanks = kwargs.get('capacity_tanks', None)
        # special capacity: ued for hax, e.g. a list of multiple refittable capacities, or a list with single item for fish hold capacity of trawlers
        self.capacity_special = self.unpack_pipe_separated_config_item_as_list('capacity_special')
        self.capacity_freight = self.get_capacity_freight()
        self.default_cargo = kwargs.get('default_cargo', None)
        self.loading_speed = kwargs.get('loading_speed', None)
        self.buy_menu_bb_xy = kwargs.get('buy_menu_bb_xy')
        self.buy_menu_width = kwargs.get('buy_menu_width', None)
        self.offsets = self.unpack_pipe_separated_config_item_as_list('offsets')
        self.graphic_variations_by_date = self.get_graphic_variations_by_date()
        self.inland_capable = kwargs.get('inland_capable', None)
        self.sea_capable = kwargs.get('sea_capable', None)
        self.register()

        """
        ship_file = codecs.open(os.path.join('src','ships',(self.id + '.py')),'w','utf8')
        foo = 'ship = Ship(id = ' + self.id + ',\n'
        for i in vars(self):
            if i is not 'id':
                foo = foo + '            ' + i + ' = ' + repr(vars(self)[i]) + ', \n'
        foo = foo + ')'
        ship_file.write(foo)
        ship_file.close()
        """

    def register(self):
        registered_ships.append(self)

    def unpack_pipe_separated_config_item_as_list(self, config_item_id):
        # a squirrely function to unpack some nasty representations of lists of lists from config item, '|' and ' ' separated
        result = []
        config_item = config.get(self.id, config_item_id)
        if len(config_item) == 0:
            return result

        for i in config_item.split('|'):
            if ' ' in i: # it's another list, separated on ' '
                result.append([int(j) for j in i.split(' ')])
            else:
                result.append(int(i))
        return result

    def get_graphic_variations_by_date(self):
        # ships have option to show random graphic variations, each variation can be date-limited
        dates_per_variation = self.unpack_pipe_separated_config_item_as_list('sprite_variation_dates')
        if len(dates_per_variation) == 0:
            dates_per_variation = [[0, 9999]] # default  one variation with min / max dates if none provided by config

        # find all the unique dates that will need a switch constructing
        triggers = reduce(set.union, dates_per_variation, set())

        # put the data in a format that's easy to render as switches
        sprite_variation_trigger_dates = {}
        for date in triggers:
            if date != 9999: # shonky magic special casing for case of no end date - not used in nml, just for convenience in the config file
                sprite_variation_trigger_dates[date] = [counter for counter, (start, end) in enumerate(dates_per_variation) if date in range(start, end)]
        return [dates_per_variation, sprite_variation_trigger_dates]

    def get_date_ranges_for_random_variation(self, index):
        years = sorted(self.graphic_variations_by_date[1].keys())
        intro = years[index]
        expiry = years[index + 1] - 1
        return str(intro) + '..' + str(expiry) + ':' + self.id + '_switch_graphics_random_' + str(intro)

    def get_ocean_speed(self):
        return (0.8, 1)[self.sea_capable]

    def get_canal_speed(self):
        return (0.7, 1)[self.inland_capable]

    def get_speeds_adjusted_for_load_amount(self, speed_index):
        # ships may travel faster or slower than 'speed' depending on cargo amount
        speeds_adjusted = (
            ((self.speed_unladen * 100 + self.speed * 0) * 32 + 9) / 1000,
            ((self.speed_unladen * 75 + self.speed * 25) * 32 + 9) / 1000,
            ((self.speed_unladen * 50 + self.speed * 50) * 32 + 9) / 1000,
            ((self.speed_unladen * 25 + self.speed * 75) * 32 + 9) / 1000,
            ((self.speed_unladen * 0 + self.speed * 100) * 32 + 9) / 1000,
        )
        speed_factors = [0.67, 1, 1.33] # there is a speed adjustment parameter, use that to look up a speed factor
        speeds_adjusted_rounded = [int(math.ceil(i * speed_factors[speed_index])) for i in speeds_adjusted] # allow that integer maths is needed for newgrf cb results; rounding up for safety
        return speeds_adjusted_rounded

    def get_adjusted_model_life(self):
        # handles keeping the buy menu tidy, relies on magic from Eddi
        if self.replacement_id != None and self.replacement_id != '-none' and self.replacement_id != '':
            for i in registered_ships:
                if i.id == self.replacement_id:
                    model_life = i.intro_date - self.intro_date
                    return model_life + self.vehicle_life
        else:
            return 'VEHICLE_NEVER_EXPIRES'

    def get_running_cost(self):
        # calculate a running cost
        fixed_run_cost = self.fixed_run_cost_factor * global_constants.FIXED_RUN_COST
        fuel_run_cost =  self.fuel_run_cost_factor * self.gross_tonnage * global_constants.FUEL_RUN_COST
        calculated_run_cost = int((fixed_run_cost + fuel_run_cost) / 98) # divide by magic constant to get costs as factor in 0-255 range
        return min(calculated_run_cost, 255) # cost factor is a byte, can't exceed 255

    def get_capacity_freight(self):
        # freight capacity is usually determined by holds, except for special cases
        if self.supertype == 'tanker':
            return self.capacity_tanks
        elif self.supertype == 'pax_mail':
            return 0
        else:
            return self.capacity_cargo_holds

    def get_default_cargo_capacity(self):
        # for ships with subtype refits for capacity, only capacity_special should be used, irrespective of cargo
        if self.str_type_info.lower() in global_constants.types_with_subtype_refits_for_capacity:
            return self.capacity_special[0]
        # otherwise the default capacity should be determined with respect to the default cargo
        if self.default_cargo == 'PASS':
            return self.capacity_pax
        elif self.default_cargo == 'MAIL':
            return self.capacity_mail
        elif self.default_cargo == 'FISH':
            return self.capacity_special[0]
        else:
            return self.capacity_freight

    def get_refittable_classes(self):
        # work out which classes are refittable based on the ship supertype
        cargo_classes = []
        for i in global_constants.class_refit_groups_by_supertype[self.supertype]:
            [cargo_classes.append(cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes)) # use set() here to dedupe

    def get_label_refits_allowed(self):
        return ','.join(global_constants.label_refits_allowed_by_supertype[self.supertype])

    def get_label_refits_disallowed(self):
        return ','.join(global_constants.label_refits_disallowed_by_supertype[self.supertype])

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        return self.title.split('[')[0]

    def get_str_name_suffix(self):
        # used in vehicle name string only, relies on name property value being in format "Foo [Bar]" for Name [Type Suffix]
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return 'STR_NAME_SUFFIX_' + type_suffix

    def get_str_type_info(self):
        # makes a string id for nml
        return 'STR_' + self.str_type_info

    def get_name(self):
        return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        cargo_units = None # only used when needed
        if self.supertype == 'packet':
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_PACKET,${capacity_mail},${capacity_cargo_holds}))"
            )
        elif self.supertype == 'trawler':
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_TRAWLER,${capacity_pax},${capacity_mail},${capacity_cargo_holds}))"
            )
        elif self.str_type_info.lower() in global_constants.types_with_subtype_refits_for_capacity:
            cargo_units = global_constants.refittable_types_cargo_strings_buy_menu[self.str_type_info.lower()]
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_GENERIC_REFIT_SUBTYPE_BUY_MENU_INFO,${capacity_special_0},${capacity_special_1},${capacity_special_2},string(${cargo_units})))"
            )
        else:
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_EMPTY))"
            )
        # dirty nasty code to handle case where capacity_special is an empty list
        capacity_special_0 = self.capacity_special[0] if len(self.capacity_special) > 0 else ''
        capacity_special_1 = self.capacity_special[1] if len(self.capacity_special) > 1 else ''
        capacity_special_2 = self.capacity_special[2] if len(self.capacity_special) > 2 else ''

        return buy_menu_template.substitute(str_type_info=self.get_str_type_info(), capacity_pax=self.capacity_pax, capacity_mail=self.capacity_mail,
                                            capacity_cargo_holds=self.capacity_cargo_holds, capacity_special_0=capacity_special_0,
                                            capacity_special_1=capacity_special_1, capacity_special_2=capacity_special_2, cargo_units=cargo_units)

    def get_cargo_suffix(self):
        return 'string(' + global_constants.refittable_types_cargo_strings_refit_menu[self.str_type_info.lower()] + ')'

    def render(self):
        template = templates[(self.custom_template or 'ship_template.pynml')]
        return template(vehicle = self)