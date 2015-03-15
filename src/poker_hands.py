#/usr/bin/env python

from enum import Enum

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

def rank(cards):
    return sorted(cards)

def isFlush(cards):
    num_hearts, num_spades, num_clubs, num_diamonds = 0
    for card in cards:
        if card.suit == Suit.diamonds:
            num_diamonds += 1
        if card.suit == Suit.spades:
            num_spades += 1
        if card.suit == Suit.diamonds:

    
def isStraight(cards):
    if type(cards) == list:
        pass
    else: 
        pass
    



