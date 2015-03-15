#/usr/bin/env python

from enum import Enum

class Suit(Enum):
    hearts, spades, diamonds, clubs = range(4)
    def __str__(self):
        if self == Suit.hearts:
            return "♥"
        if self == Suit.spades:
            return "♠"
        if self == Suit.diamonds:
            return "♦"
        if self == Suit.clubs:
            return "♣"
        return "x"

class Card(object):
    val = 0
    suit = 0
    def __init__(self,val,suit):
        self.val = val
        self.suit = Suit.hearts

    def __str__(self):
        if self.val < 11:
            return(str(self.val) + str(self.suit))
        else:
            faces = ["J","Q","K","A"]
            return(faces[self.val-11] + str(self.suit))




