#!/usr/bin/env python

print "[PARSE CONFIG] FISH.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path


# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}

import ship
from ship import Ship
from ships import registered_ships

from rosters import registered_rosters

from rosters import brit

def get_ships_in_buy_menu_order():
    sorted_ships = []
    # first compose the buy menu order list
    buy_menu_sort_order = list(registered_rosters['brit'].buy_menu_sort_order) # copy the list to avoid unwanted modifications to it
    for id in buy_menu_sort_order:
        found = False
        for ship in registered_ships:
            if ship.id == id:
                sorted_ships.append(ship)
                found = True
        if not found:
            utils.echo_message("Warning: ship " + id + " in buy_menu_sort_order, but not found in registered_ships")
    return sorted_ships

