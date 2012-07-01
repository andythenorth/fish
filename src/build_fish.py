#!/usr/bin/env python

print "build_fish.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs #used for writing files - more unicode friendly than standard open() module

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
        self.numeric_id = config.getint(id, 'numeric_id')
        self.intro_date = config.getint(id, 'intro_date')
        self.refittable_classes = global_constants.standard_class_refits['default']['allow']
        self.non_refittable_classes = global_constants.standard_class_refits['default']['disallow']
        self.allowed_cargos = '' # ! unfinished
        self.disallowed_cargos = '' # ! unfinished
        self.model_life = 254 #global_constants.model_lives[config.get(id, 'model_life')] # ! unfinished
        self.vehicle_life = 254 #global_constants.vehicle_lives[config.get(id, 'vehicle_life')] # ! unfinished
        self.speed = config.getint(id, 'speed')
        self.buy_cost = self.get_buy_cost()
        self.run_cost_override = config.getfloat(id, 'run_cost_override')
        self.capacity = 10 # !temp value
        self.buy_menu_offsets = [int(i) for i in config.get(id, 'buy_menu_offsets').split(' ')]
        self.offsets = []
        for i in config.get(id, 'offsets').split('|'):
            self.offsets.append([int(j) for j in i.split(' ')])
        self.str_type_info = config.get(id, 'str_type_info').upper()
        self.str_propulsion = config.get(id, 'str_propulsion').upper()

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

    def get_buy_menu_string(self):
        # this is an intricate function to set buy menu texts according to various truck properties :P
        from string import Template
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(STR_${str_type_info}), string(STR_${str_propulsion}))"
        )
        return buy_menu_template.substitute(str_type_info=self.str_type_info, str_propulsion=self.str_propulsion)

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
