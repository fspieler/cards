#/usr/bin/env python3

import functools
import itertools
import copy
from card import *
from orderedCards import *

class HandType(Enum):
    royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair, high_card = range(10,0,-1)
    def __str__(self):
        if self is HandType.straight_flush:
            return "straight flush"
        if self is HandType.four_of_a_kind:
            return "four of a kind"
        if self is HandType.full_house:
            return "full house"
        if self is HandType.flush:
            return "flush"
        if self is HandType.straight:
            return "straight"
        if self is HandType.three_of_a_kind:
            return "three of a kind"
        if self is HandType.two_pair:
            return "two pair"
        if self is HandType.pair:
            return "pair"
        if self is HandType.high_card:
            return "high card"
        return "x"
    def __repr__(self):
        return self.__str__()

class Hand(object):
    def __init__(self,handType,vals,cards):
        self.handType = handType
        self.vals = vals
        self.cards = cards 
    def __str__(self):
        return str(self.handType) + ": " + str(self.cards)
    def __repr__(self):
        return self.__str__()
    def __lt__(self,other):
        if self.handType.value < other.handType.value:
            return True
        elif self.handType.value > other.handType.value:
            return False
        # same hand type, go to tiebreaker
        assert len(self.vals) == len(other.vals)
        i = 0
        while i < len(self.vals):
            if self.vals[i] < other.vals[i]:
                return True
            if other.vals[i] < self.vals[i]:
                return False
            i += 1
        return False
    def __eq__(self,other):
        if self.handType.value != other.handType.value:
            return False
        # same handType
        assert(len(self.vals) == len(other.vals))
        i = 0
        while i < len(self.vals):
            if self.vals[i] != other.vals[i]:
                return False
            i += 1
        return True

def classifyCardsByVal(cards):
    def helper(d,c):
        if c.val in d:
            d[c.val].toBottom(c)
        else:
            d[c.val] = OrderedCards([c])
        return d
    return list(functools.reduce(helper, cards, {}).values())

def classifyCardsBySuit(cards):
    def helper(d,c):
        if c.suit in d:
            d[c.suit].toBottom(c)
        else:
            d[c.suit] = OrderedCards([c])
        return d
    return list(functools.reduce(helper, cards, {}).values())

# Input dictionary, output a list of tuples corresponding to dictionary
#   key-value pairs, sorted by value, largest first
def maxCounts(l):
    if not issubclass(type(l[0][0]),Enum):
        l.sort(key=lambda tup: tup[0],reverse=True)
    return max(l,key=lambda tup: len(tup[1]))

# input is a dict with key (which can be card Suit or card val, ie 2-14/Ace)
#    and values that map to occurences in a hand
def popCardsThatAppearsAtLeastNTimes(n,l):
    l.sort(key=lambda tup: tup[0],reverse=True)
    filtered = list(filter(lambda x:len(x)>=n,l))
    if len(filtered) >= 1:
        index = l.index(filtered[0])
        return l.pop(index)
    return None

def getFullHouseOrThreeOfAKind(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(3,c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    possiblePair = popCardsThatAppearsAtLeastNTimes(2,c)
    if possiblePair is not None:
        vals.append(possiblePair[0].val)
        possiblePair.deal(2,hand)
        return Hand(HandType.full_house, vals, hand)
    single = popCardsThatAppearsAtLeastNTimes(1,c)
    vals.append(single[0].val)
    single.deal(1,hand)
    single = popCardsThatAppearsAtLeastNTimes(1,c)
    vals.append(single[0].val)
    single.deal(1,hand)
    return Hand(HandType.three_of_a_kind, vals, hand)

def getFourOfAKind(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(4,c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    single = popCardsThatAppearsAtLeastNTimes(1,c)
    vals.append(single[0].val)
    single.deal(1,hand)
    return Hand(HandType.four_of_a_kind, vals, hand)

def getTwoPairOrPair(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(2,c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    possiblePair = popCardsThatAppearsAtLeastNTimes(2,c)
    if possiblePair is not None:
        vals.append(possiblePair[0].val)
        possiblePair.deal(2,hand)
        single = popCardsThatAppearsAtLeastNTimes(1,c)
        vals.append(single[0].val)
        single.deal(1,hand)
        return Hand(HandType.two_pair, vals, hand)
    for i in range(3):
        single = popCardsThatAppearsAtLeastNTimes(1,c)
        vals.append(single[0].val)
        single.deal(1,hand)
    return Hand(HandType.pair, vals, hand)

# assume max one flush possible
def getStraightFlushOrFlush(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(5,c)
    if hand is None:
        return None
    # check for straight flush...
    c2 = classifyCardsByVal(hand)
    sf = getStraight(c2)
    if sf is not None:
        if sf.vals == [14]:
            sf.handType = HandType.royal_flush
        else:
            sf.handType = HandType.straight_flush
        return sf
    # after this point, just an ordinary flush
    hand.cards_list.sort(reverse=True)
    hand.cards_list = hand.cards_list[:5]
    vals = []
    for card in hand.cards_list:
        vals.append(card.val)
    return Hand(HandType.flush, vals, hand)

def getStraight(cards):
    c = copy.deepcopy(cards)
    c.sort(key=lambda tup:tup[0],reverse=True)
    val = c[0][0].val
    # hack to handle aces as either high or low
    if val == 14:
        acesLowCopy = copy.deepcopy(c[0])
        c.append(acesLowCopy)
    prev = -1
    consecutive = 1
    for i in range(len(c)):
        temp = c[i][0].val
        # hack to handle aces as eigther high or low
        if prev == 2 and temp == 14:
            temp = 1
        if temp == prev - 1:
            consecutive += 1
            prev = c[i][0].val
            c[i].deal(1,hand)
            if consecutive == 5:
                return Hand(HandType.straight, [val], hand)
        else:
            consecutive = 1
            prev = c[i][0].val
            val = prev
            hand = OrderedCards()
            c[i].deal(1,hand)
    return None

def evalHand(cards):
    bySuit = classifyCardsBySuit(cards)
    byVal = classifyCardsByVal(cards)
    possibleHands = []
    rf_sf_or_f = getStraightFlushOrFlush(bySuit)
    if rf_sf_or_f is not None:
        if rf_sf_or_f.handType.value >= HandType.straight_flush.value:
            return rf_sf_or_f # straight flush or royal flush
        possibleHands.append(rf_sf_or_f) # wait to see if we have a better hand
    four_oak = getFourOfAKind(byVal)
    if four_oak is not None:
        return four_oak
    fh_or_3oak = getFullHouseOrThreeOfAKind(byVal)
    if fh_or_3oak is not None:
        if fh_or_3oak.handType == HandType.full_house:
            return fh_or_3oak
        possibleHands.append(fh_or_3oak)
    straight = getStraight(byVal)
    if straight is not None:
        possibleHands.append(straight)
    if len(possibleHands) > 0:
        possibleHands.sort()
        return possibleHands.pop()
    tp_or_p = getTwoPairOrPair(byVal)
    if tp_or_p is not None:
        return tp_or_p
    cards.cards_list.sort(reverse=True)
    cards.cards_list = cards.cards_list[:5]
    vals = list(map(lambda c:c.val,cards.cards_list))
    return Hand(HandType.high_card, vals, cards)
