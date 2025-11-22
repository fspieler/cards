# /usr/bin/env python3

import functools
import copy

from cards.card import *
from cards.ordered_cards import *


class HandType(Enum):
    (
        royal_flush,
        straight_flush,
        four_of_a_kind,
        full_house,
        flush,
        straight,
        three_of_a_kind,
        two_pair,
        pair,
        high_card,
    ) = range(10, 0, -1)

    def __str__(self):
        return self.name.replace("_", " ")

    def __repr__(self):
        return self.__str__()


class Hand(object):
    def __init__(self, hand_type, vals, cards):
        self.hand_type = hand_type
        self.vals = vals
        self.cards = cards

    def __str__(self):
        return str(self.hand_type) + ": " + str(self.cards)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.hand_type.value < other.hand_type.value:
            return True
        elif self.hand_type.value > other.hand_type.value:
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

    def __eq__(self, other):
        if self.hand_type.value != other.hand_type.value:
            return False
        # same hand_type
        assert len(self.vals) == len(other.vals)
        return all(it[0] == it[1] for it in zip(self.vals, other.vals))


def classify_by_value(cards):
    def helper(d, c):
        if c.val in d:
            d[c.val].to_bottom(c)
        else:
            d[c.val] = OrderedCards([c])
        return d

    return list(functools.reduce(helper, cards, {}).values())


def classify_by_suit(cards):
    def helper(d, c):
        if c.suit in d:
            d[c.suit].to_bottom(c)
        else:
            d[c.suit] = OrderedCards([c])
        return d

    return list(functools.reduce(helper, cards, {}).values())


# Input dictionary, output a list of tuples corresponding to dictionary
#   key-value pairs, sorted by value, largest first
def maxCounts(l):
    if not issubclass(type(l[0][0]), Enum):
        l.sort(key=lambda tup: tup[0], reverse=True)
    return max(l, key=lambda tup: len(tup[1]))


# input is a dict with key (which can be card Suit or card val, ie 2-14/Ace)
#    and values that map to occurences in a hand
def popCardsThatAppearsAtLeastNTimes(n, l):
    l.sort(key=lambda tup: tup[0], reverse=True)
    filtered = list(filter(lambda x: len(x) >= n, l))
    if len(filtered) >= 1:
        index = l.index(filtered[0])
        return l.pop(index)
    return None


def check_fullhouse_or_3ofakind(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(3, c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    possiblePair = popCardsThatAppearsAtLeastNTimes(2, c)
    if possiblePair is not None:
        vals.append(possiblePair[0].val)
        possiblePair.deal(2, hand)
        return Hand(HandType.full_house, vals, hand)
    single = popCardsThatAppearsAtLeastNTimes(1, c)
    vals.append(single[0].val)
    single.deal(1, hand)
    single = popCardsThatAppearsAtLeastNTimes(1, c)
    vals.append(single[0].val)
    single.deal(1, hand)
    return Hand(HandType.three_of_a_kind, vals, hand)


def check_4ofakind(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(4, c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    single = popCardsThatAppearsAtLeastNTimes(1, c)
    vals.append(single[0].val)
    single.deal(1, hand)
    return Hand(HandType.four_of_a_kind, vals, hand)


def check_twopair_or_pair(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(2, c)
    if hand is None:
        return None
    vals.append(hand[0].val)
    possiblePair = popCardsThatAppearsAtLeastNTimes(2, c)
    if possiblePair is not None:
        vals.append(possiblePair[0].val)
        possiblePair.deal(2, hand)
        single = popCardsThatAppearsAtLeastNTimes(1, c)
        vals.append(single[0].val)
        single.deal(1, hand)
        return Hand(HandType.two_pair, vals, hand)
    for i in range(3):
        single = popCardsThatAppearsAtLeastNTimes(1, c)
        vals.append(single[0].val)
        single.deal(1, hand)
    return Hand(HandType.pair, vals, hand)


# assume max one flush possible
def check_straightflush_or_flush(cards):
    c = copy.deepcopy(cards)
    vals = []
    hand = popCardsThatAppearsAtLeastNTimes(5, c)
    if hand is None:
        return None
    # check for straight flush...
    c2 = classify_by_value(hand)
    sf = check_straight(c2)
    if sf is not None:
        if sf.vals == [14]:
            sf.hand_type = HandType.royal_flush
        else:
            sf.hand_type = HandType.straight_flush
        return sf
    # after this point, just an ordinary flush
    hand.cards_list.sort(reverse=True)
    hand.cards_list = hand.cards_list[:5]
    vals = []
    for card in hand.cards_list:
        vals.append(card.val)
    return Hand(HandType.flush, vals, hand)


def check_straight(cards):
    c = copy.deepcopy(cards)
    c.sort(key=lambda tup: tup[0], reverse=True)
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
            c[i].deal(1, hand)
            if consecutive == 5:
                return Hand(HandType.straight, [val], hand)
        else:
            consecutive = 1
            prev = c[i][0].val
            val = prev
            hand = OrderedCards()
            c[i].deal(1, hand)
    return None


def eval_hand(cards):
    by_suit = classify_by_suit(cards)
    by_value = classify_by_value(cards)
    possible_hands = []
    rf_sf_or_f = check_straightflush_or_flush(by_suit)
    if rf_sf_or_f is not None:
        if rf_sf_or_f.hand_type.value >= HandType.straight_flush.value:
            return rf_sf_or_f  # straight flush or royal flush
        possible_hands.append(rf_sf_or_f)  # wait to see if we have a better hand
    four_oak = check_4ofakind(by_value)
    if four_oak is not None:
        return four_oak
    fh_or_3oak = check_fullhouse_or_3ofakind(by_value)
    if fh_or_3oak is not None:
        if fh_or_3oak.hand_type == HandType.full_house:
            return fh_or_3oak
        possible_hands.append(fh_or_3oak)
    straight = check_straight(by_value)
    if straight is not None:
        possible_hands.append(straight)
    if possible_hands:
        possible_hands.sort()
        return possible_hands.pop()
    tp_or_p = check_twopair_or_pair(by_value)
    if tp_or_p is not None:
        return tp_or_p
    cards.cards_list.sort(reverse=True)
    cards.cards_list = cards.cards_list[:5]
    vals = list(map(lambda c: c.val, cards.cards_list))
    return Hand(HandType.high_card, vals, cards)

def holdem_monte_carlo(deck, community, n, *hands):
    winners = [0] * len(hands)
    assert len(community) < 5
    for _ in range(n):
        d = copy.deepcopy(deck)
        d.shuffle()
        h = copy.deepcopy(hands)
        c = copy.deepcopy(community)
        d.deal(5-len(c), c)
        for hand in h:
            hand += c
        evaluated_hands = [eval_hand(it) for it in h]
        winning_hand = max(evaluated_hands)
        num_winning = len([it for it in evaluated_hands if it == winning_hand])
        winning_points = 1 / num_winning
        for idx, hand in enumerate(evaluated_hands):
            if hand == winning_hand:
                winners[idx] += winning_points
    return [it / n for it in winners]



