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

# get the globals - however for using globals in templates, it's better for the template to use global_template.pt as a macro
import global_constants # expose all constants for easy passing to templates

import utils

# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}

import ship
from ship import Ship
from ships import registered_ships

from ships import altamira_freighter
from ships import barletta_paddle_steamer
from ships import cape_spear_trawler
from ships import capo_sandalo_vehicle_ferry
from ships import castle_point_steamer
from ships import eddystone_tanker
from ships import endeavour_utility_catamaran
from ships import enoshima_catamaran_ferry
from ships import fastnet_paddle_steamer
from ships import feodosiya_hydrofoil
from ships import fish_island_trawler
from ships import frisco_bay_freighter
from ships import harbour_point_utility_vessel
from ships import hopetown_tanker
from ships import lindau_freight_barge
from ships import little_cumbrae_freighter
from ships import marstein_freighter
from ships import maspalomas_freighter
from ships import matsushima_hydrofoil
from ships import mount_blaze_catamaran_ferry
from ships import nieuwpoort_container_feeder
from ships import patos_island_vehicle_ferry
from ships import pine_island_log_tug
from ships import saint_marie_barge_tug
from ships import santorini_freighter
from ships import shark_island_livestock_ship
from ships import sunk_rock_ferry
from ships import thunder_bay_hovercraft
from ships import whitgift_freight_barge
from ships import yokohama_tanker


def get_ships_in_buy_menu_order():
    sorted_ships = []
    for id in global_constants.buy_menu_sort_order:
        found = False
        for ship in registered_ships:
            if ship.id == id:
                sorted_ships.append(ship)
                found = True
        if not found:
            utils.echo_message("Warning: ship " + id + " in buy_menu_sort_order, but not found in registered_ships")
    return sorted_ships

