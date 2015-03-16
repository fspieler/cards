#/usr/bin/env python

from orderedCards import *

class Hand(Enum):
    straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, one_pair, high_card = range(9,0,-1)
    def __str__(self):
        if self is Hand.straight_flush:
            return "straight flush"
        if self is Hand.four_of_a_kind:
            return "four of a kind"
        if self is Hand.full_house:
            return "full house"
        if self is Hand.flush:
            return "flush"
        if self is Hand.straight:
            return "straight"
        if self is Hand.three_of_a_kind:
            return "three of a kind"
        if self is Hand.two_pair:
            return "two pair"
        if self is Hand.high_card:
            return "high card"
        return "x"

def suitEvaluator(cards): 
    return lambda suit : {x for x in cards if x.suit == suit}
def valueFilter(cards): 
    return lambda value : {x for x in cards if x.value == value}
    

def hearts(cards): 
    return suitEvaluator(Suit.hearts)(cards)
def clubs(cards):
    return suitEvaluator(Suit.clubs)(cards)
def diamonds(cards):
    return suitEvaluator(Suit.diamonds)(cards)
def spades(cards):
    return suitEvaluator(Suit.spades)(cards)

def ones(cards): 
    return valueFilter(1)(cards)
def twos(cards): 
    return valueFilter(2)(cards)
def three(cards):
    return valueFilter(3)(cards)


def suitSet(cards):
    return {
            'hearts': {x for x in cards if x.suit == Suit.hearts},
            'spades' : {x for x in cards if x.suit == Suit.spades},
            'diamonds' : {x for x in cards if x.suit == Suit.diamonds},
            'clubs' : {x for x in cards if x.suit == Suit.clubs},
            }

def valSet(cards):
    return {
            'twos': {x for x in cards if x.val == 2},
            'threes': {x for x in cards if x.val == 3},
            'fours': {x for x in cards if x.val == 4},
            'fives': {x for x in cards if x.val == 5},
            'sixes': {x for x in cards if x.val == 6},
            'sevens': {x for x in cards if x.val == 7},
            'eights': {x for x in cards if x.val == 8},
            'nines': {x for x in cards if x.val == 9},
            'tens': {x for x in cards if x.val == 10},
            'jacks': {x for x in cards if x.val == 11},
            'queens': {x for x in cards if x.val == 12},
            'kings': {x for x in cards if x.val == 13},
            'aces': {x for x in cards if x.val == 14}
            }


