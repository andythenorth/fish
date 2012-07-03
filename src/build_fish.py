#!/usr/bin/env python

print "build_fish.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs #used for writing files - more unicode friendly than standard open() module
import math

from chameleon import PageTemplateLoader
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'), format='text')
lang_templates = PageTemplateLoader(os.path.join(currentdir, 'lang'), format='text')
docs_templates = PageTemplateLoader(os.path.join(currentdir,'docs'), format='text')


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
        self.vehicle_type = 'ship'
        self.id = id

        #setup properties for this vehicle
        self.title = config.get(id, 'title')
        self.numeric_id = config.get(id, 'numeric_id')
        self.intro_date = config.getint(id, 'intro_date')
        self.model_life = config.getint(id, 'vehicle_life')
        if self.model_life == 255:
            self.model_life = 'VEHICLE_NEVER_EXPIRES'
        self.vehicle_life = config.getint(id, 'vehicle_life')
        self.speed = config.getfloat(id, 'speed')
        self.speed_unladen = self.speed * config.getfloat(id, 'speed_factor_unladen')
        self.buy_cost = self.get_buy_cost()
        self.run_cost_override = config.getfloat(id, 'run_cost_override')
        self.capacity_pax = config.getint(id, 'capacity_pax')
        self.capacity_mail = config.getint(id, 'capacity_mail')
        self.capacity_freight = config.getint(id, 'capacity_freight')
        self.default_cargo = config.get(id, 'default_cargo')
        self.allowed_cargos = '' # ! unfinished
        self.disallowed_cargos = '' # ! unfinished
        self.buy_menu_bb_xy = [int(i) for i in config.get(id, 'buy_menu_bb_xy').split(' ')]
        self.offsets = []
        for i in config.get(id, 'offsets').split('|'):
            self.offsets.append([int(j) for j in i.split(' ')])
        self.str_type_info = config.get(id, 'str_type_info').upper()
        self.str_propulsion = config.get(id, 'str_propulsion').upper()
        self.inland_capable = config.getboolean(id, 'inland_capable')
        self.sea_capable = config.getboolean(id, 'sea_capable')

    def get_ocean_speed(self):
        return (0.9, 1)[self.sea_capable]

    def get_canal_speed(self):
        return (0.9, 1)[self.inland_capable]

    def get_speeds_adjusted_for_load_amount(self):
        # ships may travel faster or slower than 'speed' depending on cargo amount
        speeds_adjusted = (
            ((self.speed_unladen * 100 + self.speed * 0) * 32 + 9) / 1000,
            ((self.speed_unladen * 75 + self.speed * 25) * 32 + 9) / 1000,
            ((self.speed_unladen * 50 + self.speed * 50) * 32 + 9) / 1000,
            ((self.speed_unladen * 25 + self.speed * 75) * 32 + 9) / 1000,
            ((self.speed_unladen * 0 + self.speed * 100) * 32 + 9) / 1000,
        )
        speeds_adjusted_rounded = [int(math.ceil(i)) for i in speeds_adjusted] # allow that integer maths is needed for newgrf cb results; rounding up for safety
        return speeds_adjusted_rounded

    def get_buy_cost(self):
        # if buy cost override is 0 (i.e. not defined), calculate the buy cost, otherwise use the value of cost override
        buy_cost_override = config.getint(self.id, 'buy_cost_override')
        if buy_cost_override == 0:
            # !provide a calculation of cost
            return 10
        else:
            return buy_cost_override

    def get_running_cost(self):
        # if buy cost is 0 (i.e. not defined), derive the buy cost, otherwise use the defined cost
        if self.run_cost_override == 0:
            # calculate a running cost based on power and a multiplier value
            return 10 # !temp value
        else:
            return self.run_cost_override

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
        # assumes (1) freight ships refittable to most classes (2) that certain combinations of capacity don't need to be handled
        if self.capacity_pax > 0 and self.capacity_mail > 0 and self.capacity_freight > 0:
            return global_constants.standard_class_refits['all']
        elif self.capacity_pax == 0 and self.capacity_mail == 0:
            return global_constants.standard_class_refits['all_but_pax_mail']
        elif self.capacity_pax == 0 and self.capacity_mail > 0:
            return global_constants.standard_class_refits['all_but_pax']
        elif self.capacity_pax > 0 and self.capacity_mail > 0 and self.capacity_freight == 0 :
            return global_constants.standard_class_refits['pax_mail_only']
        else:
            raise # must be a combination I haven't thought of, or user error in the config

    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        from string import Template
        if self.capacity_pax > 0 and self.capacity_freight > 0:
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(STR_${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES,${capacity_pax},${capacity_freight}), string(STR_${str_propulsion}))"
            )
        else:
            buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(STR_${str_type_info}), string(STR_EMPTY), string(STR_${str_propulsion}))"
            )

        return buy_menu_template.substitute(str_type_info=self.str_type_info, str_propulsion=self.str_propulsion, capacity_pax=self.capacity_pax, capacity_freight=self.capacity_freight)

    def render(self):
        template = templates['ship_template.pynml']
        return template(vehicle = self)


#compose vehicle objects into a list; order is not significant as numeric identifiers are used to build vehicles
vehicles = []
for i in config.sections():
    if i not in global_constants.vehicles_turned_off:
        vehicles.append(Ship(id=i))

#compile a single final nml file for the grf
master_template = templates['fish.pynml']

grf_nml = codecs.open(os.path.join('fish.nml'),'w','utf8')
grf_nml.write(master_template(vehicles=vehicles, repo_vars=repo_vars))
grf_nml.close()


#compile strings to single lang file (english only at the moment, but i18n translation is possible)
lang_template = lang_templates['english.pylng']

lang = codecs.open(os.path.join('lang','english.lng'), 'w','utf8')
lang.write(lang_template(vehicles=vehicles, repo_vars=repo_vars))
lang.close()


#compile docs (english only at the moment, but i18n translation is possible)
docs_template = docs_templates['readme.pytxt']

docs = codecs.open(os.path.join('docs','readme.txt'), 'w','utf8')
docs.write(docs_template(vehicles=vehicles, repo_vars=repo_vars))
docs.close()
