print "[RENDER DOCS] render_docs.py"

import FISH
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(currentdir,'docs_src'))

vehicles = FISH.get_vehicles()
# default sort for docs is by vehicle intro date
vehicles = sorted(vehicles, key=lambda vehicle: vehicle.intro_date)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

# compile docs (english only at the moment, but i18n translation is possible)
readme_template = docs_templates['readme.pytxt']
readme = codecs.open(os.path.join('docs','readme.txt'), 'w','utf8')
readme.write(readme_template(vehicles=vehicles, repo_vars=repo_vars))
readme.close()

set_overview_template = docs_templates['set_overview.pt']
set_overview = codecs.open(os.path.join('docs','set_overview.html'), 'w','utf8')
set_overview.write(set_overview_template(vehicles=vehicles, repo_vars=repo_vars, base_lang_strings=base_lang_strings))
set_overview.close()
