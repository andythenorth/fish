#!/bin/bash
  ./src/build_fish.py \
  && nmlc fish.nml --nfo=sprites/fish.nfo \
  && grfcodec -e fish.grf \
  && mv fish.grf /Users/andy/Documents/OpenTTD/data
