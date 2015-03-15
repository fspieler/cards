#/usr/bin/env python

from enum import Enum

class Suit(Enum):
    hearts, spades, diamonds, clubs = range(4)
    def __str__(self):
        if self is Suit.hearts:
            return "♥"
        if self is Suit.spades:
            return "♠"
        if self is Suit.diamonds:
            return "♦"
        if self is Suit.clubs:
            return "♣"
        return "x"

class Card(object):
    val = 0
    suit = -1
    def __init__(self,val,suit):
        self.val = val
        if(not type(suit) is Suit):
            self.suit = Suit(suit)
        else:
            self.suit = suit

    def __str__(self):
        if self.val < 11:
            return(str(self.val) + str(self.suit))
        else:
            faces = ["J","Q","K","A"]
            return(faces[self.val-11] + str(self.suit))

