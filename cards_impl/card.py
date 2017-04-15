#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

def cards():
    class Object(object):
        pass
    cards = Object()
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    # Note that `suits` order must be consistent with the Suit enum order!
    suits = ['h', 's', 'd', 'c']
    for num_idx, num in enumerate(numbers):
        for suit_idx, suit in enumerate(suits):
            # add 2 to num_idex since Card wants a number starting from 2
            setattr(cards,'_'+num+suit,Card(num_idx+2, suit_idx))
    return cards

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
        if not (2 <= val <= 14):
            raise ValueError("Card constructor only accepts vals between 2 and 14; given value :" + str(val))
        self.val = val
        if(type(suit) is Suit):
            self.suit = suit
        else:
            self.suit = Suit(suit)

    def __str__(self):
        # adds ANSI-coloring
        blackStr = lambda s : "\033[0m"+s+"\033[0m"
        redStr = lambda s : "\033[1;31m"+s+"\033[0m"
        color = redStr if (self.suit in (Suit.hearts, Suit.diamonds)) else blackStr
        if self.val < 11: # not a face card
            return(color(str(self.val) + str(self.suit)))
        else:
            faces = ["J","Q","K","A"]
            return(color(faces[self.val-11] + str(self.suit)))

    def __repr__(self):
        return self.__str__()

    def __gt__(self,other):
        return self.val > other.val

    def __lt__(self,other):
        return self.val < other.val

    def __eq__(self,other):
        return isinstance(other,type(self)) \
                and (self.val, self.suit) == (other.val, other.suit)

    def __hash__(self):
        return hash(self.val) ^ hash(self.suit) ^ hash((self.val,self.suit))
