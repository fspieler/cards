#!/usr/bin/env python3

from enum import Enum

def blackStr(string):
    return "\033[0m"+string+"\033[0m"

def redStr(string):
    return "\033[1;31m"+string+"\033[0m"

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
        return "x" # shouldn't be reached!

class Card(object):
    def __init__(self,val,suit=None):
        if(type(val) is tuple):
            suit = Suit(val[1])
            val = val[0]
        self.val = val
        if(not type(suit) is Suit):
            self.suit = Suit(suit)
        else:
            self.suit = suit

    def __str__(self):
        color = redStr if (self.suit in (Suit.hearts, Suit.diamonds)) else blackStr
        if self.val < 11: # not a face card
            return(color(str(self.val) + str(self.suit)))
        else:
            faces = ["J","Q","K","A"]
            return(color(faces[self.val-11] + str(self.suit)))

    def __gt__(self,other):
        return self.val > other.val

    def __lt__(self,other):
        return self.val < other.val

    def __eq__(self,other):
        return isinstance(other,type(self)) \
                and (self.val, self.suit) == (other.val, other.suit)

    def __hash__(self):
        return hash(self.val) ^ hash(self.suit) ^ hash((self.val,self.suit))
