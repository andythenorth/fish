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

# changing the order of rosters breaks savegames (parameter values change), don't do it.
from rosters import brit
from rosters import euro

def get_ships_in_buy_menu_order(show_warnings=False):
    sorted_ships = []
    buy_menu_sort_order = []
    # first compose the buy menu order list
    for roster in registered_rosters:
        buy_menu_sort_order.extend(roster.buy_menu_sort_order)

    for id in buy_menu_sort_order:
        found = False
        for ship in registered_ships:
            if ship.id == id:
                sorted_ships.append(ship)
                found = True
        if not found:
            utils.echo_message("Warning: ship " + id + " in buy_menu_sort_order, but not found in registered_ships")

    # now guard against any ships missing from buy menu order, as that wastes time asking 'wtf?' when they don't appear in game
    for ship in registered_ships:
        id = ship.id
        if show_warnings and id not in buy_menu_sort_order:
            utils.echo_message("Warning: ship " + id + " in registered_ships, but not in buy_menu_sort_order - won't show in game")
    return sorted_ships

