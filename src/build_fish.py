#!/usr/bin/env python

print "build_fish.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module
import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))
lang_templates = PageTemplateLoader(os.path.join(currentdir, 'lang_src'))
docs_templates = PageTemplateLoader(os.path.join(currentdir,'docs'))


# the parser handles config file formats; provides a custom utility function for parsing to a list
import ConfigParser

import re
pattern = re.compile('\\d+$') #regular expressions magic: pattern of digits
def config_option_to_list_of_ints(txt):
    result = [] # we always want at minimum an empty list here or other code will be sad
    for i in txt.split('|'):
        m = pattern.match(i)
        if m:
            result.append(int(i))
    return result

config = ConfigParser.RawConfigParser()
config.read(os.path.join(currentdir, 'src', 'FISH.cfg'))


# get the globals - however for using globals in templates, it's better for the template to use global_template.pt as a macro
import global_constants # expose all constants for easy passing to templates

# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}


class Ship(object):
    """Base class for all types of ships"""
    def __init__(self, id):
        self.id = id

        #setup properties for this vehicle
        self.title = config.get(id, 'title')
        self.numeric_id = config.get(id, 'numeric_id')
        if config.get(id, 'custom_template').strip() != '':
            self.custom_template = config.get(id, 'custom_template')
        else:
            self.custom_template = None
        self.str_type_info = config.get(id, 'str_type_info').upper()
        # supertype controls refits etc, so figure it out from the type
        self.supertype = {'hydrofoil_fast_ferry':'pax_mail',
                          'catamaran_fast_ferry':'packet',
                          'small_general_purpose_vessel':'packet',
                          'vehicle_ferry':'packet',
                          'paddle_steamer':'packet',
                          'cargo_vessel_inland':'gcv',
                          'log_tug':'log_tug',
                          'cargo_hovercraft':'gcv',
                          'small_coaster':'gcv',
                          'coaster':'gcv',
                          'large_coaster':'gcv',
                          'small_coastal_tanker':'tanker',
                          'coastal_tanker':'tanker',
                          'large_coastal_tanker':'tanker',
                          'trawler':'trawler',
                          'livestock_ship':'livestock_ship',
                          'rig_supply_fast_catamaran':'packet',
                          'barge_tug':'gcv',
                          'container_feeder':'container_feeder'}[self.str_type_info.lower()]
        self.graphics_template = config.get(id, 'graphics_template')
        self.intro_date = config.getint(id, 'intro_date')
        self.replacement_id = config.get(id, 'replacement_id')
        #print self.replacement_id
        self.vehicle_life = config.getint(id, 'vehicle_life')
        self.speed = config.getfloat(id, 'speed')
        self.speed_unladen = self.speed * config.getfloat(id, 'speed_factor_unladen')
        self.buy_cost = config.getint(id, 'buy_cost')
        self.fixed_run_cost_factor = config.getfloat(id, 'fixed_run_cost')
        self.fuel_run_cost_factor = config.getfloat(id, 'fuel_run_cost')
        self.gross_tonnage = config.getint(id, 'gross_tonnage')
        self.capacity_pax = config.getint(id, 'capacity_pax')
        self.capacity_mail = config.getint(id, 'capacity_mail')
        self.capacity_cargo_holds = config.getint(id, 'capacity_cargo_holds')
        self.capacity_tanks = config.getint(id, 'capacity_tanks')
        self.capacity_freight = self.get_capacity_freight()
        self.default_cargo = config.get(id, 'default_cargo')
        self.loading_speed = config.get(id, 'loading_speed')
        self.allowed_cargos = '' # ! unfinished
        self.disallowed_cargos = '' # ! unfinished
        self.buy_menu_bb_xy = [int(i) for i in config.get(id, 'buy_menu_bb_xy').split(' ')]
        self.buy_menu_width = config.getint(id, 'buy_menu_width')
        self.offsets = []
        for i in config.get(id, 'offsets').split('|'):
            self.offsets.append([int(j) for j in i.split(' ')])
        self.inland_capable = config.getboolean(id, 'inland_capable')
        self.sea_capable = config.getboolean(id, 'sea_capable')

    def get_ocean_speed(self):
        return (0.8, 1)[self.sea_capable]

    def get_canal_speed(self):
        return (0.8, 1)[self.inland_capable]

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
            for i in vehicles:
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
        # the default capacity should be determined with respect to the default cargo
        if self.default_cargo == 'PASS':
            return self.capacity_pax
        elif self.default_cargo == 'MAIL':
            return self.capacity_mail
        else:
            return self.capacity_freight

    def get_refittable_classes(self):
        # work out which classes are refittable based on the ships capacities for various types of cargo
        classes = []
        if self.capacity_pax > 0:
            [classes.append(i) for i in global_constants.standard_class_refits['pax']]
        if self.capacity_mail > 0:
            [classes.append(i) for i in global_constants.standard_class_refits['mail']]
        if self.capacity_cargo_holds > 0:
            [classes.append(i) for i in global_constants.standard_class_refits['cargo_holds']]
        if self.capacity_tanks > 0:
            [classes.append(i) for i in global_constants.standard_class_refits['tanks']]
        return ','.join(set(classes)) # use set() here to dedupe

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        return self.title.split('[')[0]

    def get_name(self):
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return "string(STR_NAME_" + self.id +", string(STR_NAME_SUFFIX_" + type_suffix + "))"


    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        if self.capacity_pax > 0 and self.capacity_cargo_holds > 0:
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(STR_${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_PAX_CARGO,${capacity_pax},${capacity_cargo_holds}))"
            )
        else:
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(STR_${str_type_info}), string(STR_EMPTY))"
            )

        return buy_menu_template.substitute(str_type_info=self.str_type_info, capacity_pax=self.capacity_pax, capacity_cargo_holds=self.capacity_cargo_holds)

    def render(self):
        template = templates[(self.custom_template or 'ship_template.pynml')]
        return template(vehicle = self)


#compose vehicle objects into a list; order is not significant as numeric identifiers are used to build vehicles
config_globals = {}
for name, value in config.items('config_globals'):
    config_globals[name] = value

vehicles = []
for i in config.sections():
    if i not in global_constants.vehicles_turned_off and i != 'config_globals':
        vehicles.append(Ship(id=i))

# compile a single final nml file for the grf
master_template = templates['fish.pynml']

grf_nml = codecs.open(os.path.join('fish.nml'),'w','utf8')
templated_nml = master_template(vehicles=vehicles, repo_vars=repo_vars, config_globals = config_globals)
# an ugly hack here because chameleon html escapes some characters
templated_nml = '>'.join(templated_nml.split('&gt;'))
templated_nml = '&'.join(templated_nml.split('&amp;'))
grf_nml.write(templated_nml)
grf_nml.close()

# this is a brutally simple way of specifying which languages are available
# could also read the lang dir and work it out from .pylng extensions, but meh, tmwftlb
translated_languages = ('english', 'afrikaans', 'dutch', 'spanish')
for i in translated_languages:
    #compile strings to single lang file - english
    lang_template = lang_templates[i + '.pylng']

    lang = codecs.open(os.path.join('lang', i + '.lng'), 'w','utf8')
    lang.write(lang_template(vehicles=vehicles, repo_vars=repo_vars))
    lang.close()


# compile docs (english only at the moment, but i18n translation is possible)
docs_template = docs_templates['readme.pytxt']

docs = codecs.open(os.path.join('docs','readme.txt'), 'w','utf8')
docs.write(docs_template(vehicles=vehicles, repo_vars=repo_vars))
docs.close()
