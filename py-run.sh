#!/bin/bash

pypath=$(which python3)
realpypath="#!/$pypath"

echo "$realpypath"|cat - main.py > /tmp/out && mv /tmp/out uscan.py

echo "run uscan.py"
