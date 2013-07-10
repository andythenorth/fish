import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

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

#compose vehicle objects into a list; order is not significant as numeric identifiers are used to build vehicles
config_globals = {}
for name, value in config.items('config_globals'):
    config_globals[name] = value

vehicles = []
