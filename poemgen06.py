#!/usr/bin/python3

import json
import random

# Open my poem database
with open("poems.json") as pj:
    # Convert poems.json to pythonic data structure
    pythonpoems = json.load(pj)

# Randomly select poem from python data
# Print the randomly selected poem to the screen
(print(random.choice(list(pythonpoems.values()))))
