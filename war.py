#!/usr/bin/env python3

from lib.card import *

you = []
them = []
players = [you, them]
deck= getDeck()

deal(deck, players, int(52/len(players)))

print("you:")
printCards(you)

print("them:")
printCards(them)

