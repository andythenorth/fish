#!/usr/bin/env python

from time import time
start = time()

print "[BUILD] build_fish.py"

import FISH
import utils

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
docs_templates = PageTemplateLoader(os.path.join(currentdir,'docs_src'))

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

vehicles = FISH.get_vehicles()
config_globals = FISH.get_config_globals()

# compile a single final nml file for the grf
master_template = templates['fish.pynml']

grf_nml = codecs.open(os.path.join('fish.nml'),'w','utf8')
templated_nml = master_template(vehicles=vehicles, repo_vars=repo_vars, config_globals = config_globals)
# an ugly hack here because chameleon html escapes some characters
templated_nml = '>'.join(templated_nml.split('&gt;'))
templated_nml = '&'.join(templated_nml.split('&amp;'))
grf_nml.write(templated_nml)
grf_nml.close()

# compile lang files
import lang

# compile the docs
import docs

print (time() - start)
