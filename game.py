#!/usr/bin/env python3

import itertools, random
from pokerHands import *

# create deck
deck = getDeck()

user = OrderedCards()
deck.deal(5, user)
print("You got: " + str(user))
