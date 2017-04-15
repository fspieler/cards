#!/usr/bin/env python3

import itertools, random
from cards_impl import *
deck = getDeck()


fred = OrderedCards()
al = OrderedCards()
burn = OrderedCards()
community = OrderedCards()

deck.deal(2, al, fred)
print("Fred's hand: " + str(fred))
print("Al's hand: " + str(al))
deck.deal(1,burn)
deck.deal(3,community)
print("Flop: " + str(community))
deck.deal(1,burn)
deck.deal(1,community)
print("Turn: " + str(community))
deck.deal(1,burn)
deck.deal(1,community)
print("River: " + str(community))
com2 = OrderedCards(community.cards_list[:])
community.deal(5,fred)
com2.deal(5,al)
fredHand = evalHand(fred)
alHand = evalHand(al)
print("Fred's best hand: " + str(fredHand))
print("Al's best hand: " + str(alHand))
if fredHand > alHand:
    print("Fred wins!")
elif alHand > fredHand:
    print("Al wins!")
else:
    print("Push!")
