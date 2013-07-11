print "[RENDER NML] render_nml.py"

import fish
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

vehicles = fish.get_vehicles()

# compile a single final nml file for the grf
master_template = templates['fish.pynml']

grf_nml = codecs.open(os.path.join('fish.nml'),'w','utf8')
templated_nml = master_template(vehicles=vehicles, repo_vars=repo_vars)
# an ugly hack here because chameleon html escapes some characters
templated_nml = '>'.join(templated_nml.split('&gt;'))
templated_nml = '&'.join(templated_nml.split('&amp;'))
grf_nml.write(templated_nml)
grf_nml.close()
