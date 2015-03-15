#!/usr/bin/env python3

from lib.card import *

you = []
them = []
players = [you, them]
deck= getDeck()

deal(deck, players, 1)

print("you:")
printCards(you)

print("them:")
printCards(them)

