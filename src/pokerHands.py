#/usr/bin/env python

import functools
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

def classifyCardsByVal(cards):
    def helper(d,c):
        if c.val in d:
            d[c.val].toBottom(c)
        else:
            d[c.val] = OrderedCards([c])
        return d
    return functools.reduce(helper, cards, {})

def classifyCardsBySuit(cards):
    def helper(d,c):
        if c.suit in d:
            d[c.suit].toBottom(c)
        else:
            d[c.suit] = OrderedCards([c])
        return d
    return functools.reduce(helper, cards, {})

def dictCounts(d):
    return {k: len(v) for k,v in d.items()}

def maxCounts(d):
    pass

c = cards()
hand = [c.ha, c.sa, c.ca, c.sk, c.ck, c.
bySuit = classifyCardsBySuit()
byVal = classifyCardsByVal(hand)

