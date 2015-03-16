#!/usr/bin/env python3

import itertools, random
from src.poker_hands import *

# create deck
deck = getDeck()

user = OrderedCards()
deck.deal(5, user)
print("You got: " + str(user))
