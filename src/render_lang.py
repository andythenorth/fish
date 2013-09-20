print "[RENDER LANG] render_lang.py"

import fish
import utils

import shutil
import os
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
lang_templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'lang_templates'))

lang_src = os.path.join(currentdir, 'lang_src')
lang_dst = os.path.join(currentdir, 'lang')

if os.path.exists(lang_dst):
    shutil.rmtree(lang_dst)
shutil.copytree(lang_src, lang_dst)
codecs.open(os.path.join(lang_dst, '_lang_files_here_are_generated.txt'), 'w','utf8')

ships = fish.get_ships_in_buy_menu_order()
# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

translated_languages = ('english',)
for i in translated_languages:
    #compile strings to single lang file - english
    lang_template = lang_templates[i + '.pylng']

    src_file = codecs.open(os.path.join(lang_src, i + '.lng'), 'r','utf8')
    dst_file = codecs.open(os.path.join(lang_dst, i + '.lng'), 'w','utf8')
    lang_content = src_file.read()
    lang_content = lang_content + lang_template(ships=ships, repo_vars=repo_vars)
    dst_file.write(lang_content)
    dst_file.close()
