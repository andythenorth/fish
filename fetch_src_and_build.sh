#!/bin/bash
  curl http://213.133.67.181:8192/zz_dangerous_things/tt_foundry/sets/FISH/render_vehicles_to_config_file > src/FISH.cfg \
  && ./makefish.sh
