#!/usr/bin/env python

print "[PARSE CONFIG] FISH.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import legacy_config_handler

# get the globals - however for using globals in templates, it's better for the template to use global_template.pt as a macro
import global_constants # expose all constants for easy passing to templates

# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}

from ship import Ship

config = legacy_config_handler.config
def get_vehicles():
    return legacy_config_handler.vehicles

def get_config_globals():
    return legacy_config_handler.config_globals

vehicles = get_vehicles()
config_globals = get_config_globals()

for i in config.sections():
    if i not in global_constants.vehicles_turned_off and i != 'config_globals':
        vehicles.append(Ship(id=i))
