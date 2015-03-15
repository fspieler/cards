#!/usr/bin/env python3

import itertools, random
from lib.card import *

# create deck
deck = getDeck();

# draw five cards 
print("You got:") 
for i in range(5):
    print(deck[i])

