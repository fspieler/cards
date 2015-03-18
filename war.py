#!/usr/bin/env python3

from pokerHands import *

def war(you, them, cards=None):
    if(cards is None):
        cards=OrderedCards()
    yourCard = you.list()[0]
    you.deal(1,cards)
    theirCard = them.list()[0]
    them.deal(1,cards)
    print("Your card: " + str(yourCard))
    print("Their card: " + str(theirCard))
    if(yourCard > theirCard):
        print("You win this round and these cards: " + str(cards))
        cards.deal(len(cards),you)
        print("Card count: you -> " + str(len(you)) + ", them -> " + str(len(them)))
    elif(yourCard < theirCard):
        print("They win this round and these cards: " + str(cards))
        cards.deal(len(cards),them)
        print("Card count: you -> " + str(len(you)) + ", them -> " + str(len(them)))
    else:
        print("WAR!")
        you.deal(3, cards)
        them.deal(3, cards)
        war(you, them, cards)

you = OrderedCards()
them = OrderedCards()
players = [you, them]
deck= getDeck()

deck.deal(26, you, them)

print("you:")
print(you)

print("them:")
print(them)

while len(you) > 0 and len(them) > 0:
    war(you, them)
