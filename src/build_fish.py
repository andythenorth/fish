#!/usr/bin/env python

from time import time
start = time()

print("[BUILD] build_fish.py")

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# render the nml file
import render_nml

# render the lang files
import render_lang

# render the docs
import render_docs

print((time() - start))
