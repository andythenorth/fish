print "[RENDER DOCS] render_docs.py"

import fish
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(currentdir,'docs_src'))

ships = fish.get_ships_in_buy_menu_order()
# default sort for docs is by ship intro date
ships = sorted(ships, key=lambda ship: ship.intro_date)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

metadata = {}
dates = sorted([i.intro_date for i in ships])
metadata['dates'] = (dates[0], dates[-1])
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?f=26&t=44613'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/fish/'

# compile docs (english only at the moment, but i18n translation is possible)
readme_template = docs_templates['readme.pytxt']
readme = codecs.open(os.path.join('docs','readme.txt'), 'w','utf8')
readme.write(readme_template(ships=ships, repo_vars=repo_vars))
readme.close()

set_overview_template = docs_templates['set_overview.pt']
set_overview = codecs.open(os.path.join('docs','set_overview.html'), 'w','utf8')
set_overview.write(set_overview_template(ships=ships, repo_vars=repo_vars, base_lang_strings=base_lang_strings, metadata=metadata))
set_overview.close()
