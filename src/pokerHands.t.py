#/usr/bin/env python3

import unittest
import card
import orderedCards
from pokerHands import *

class TestCard(unittest.TestCase):

    def test_getFullHouse(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._2h, c._2d, c._2s, c._3h, c._3s, c._4s, c._4c, c._4h])
        #output_hand =  getFullHouseOrThreeOfAKind(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.full_house)
        self.assertEqual(output_hand.vals, [4,3])

    def test_getFullHouse_two(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._2h, c._2d, c._2s, c._3h, c._6s, c._as, c._ac, c._ah])
        #output_hand =  getFullHouseOrThreeOfAKind(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.full_house)
        self.assertEqual(output_hand.vals, [14,2])

    def test_getThreeOfAKind(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._2h, c._2d, c._2s, c._3h, c._6s, c._js, c._8c, c._ah])
        #output_hand =  getFullHouseOrThreeOfAKind(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.three_of_a_kind)
        self.assertEqual(output_hand.vals, [2,14,11])

    def test_getFourOfAKind(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._2h, c._2d, c._2s, c._3h, c._6s, c._js, c._8c, c._2c])
        #output_hand =  getFourOfAKind(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.four_of_a_kind)
        self.assertEqual(output_hand.vals, [2,11])

    def test_getTwoPair(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._2h, c._2d, c._3s, c._3h, c._6s, c._js, c._8c, c._7c])
        #output_hand = getTwoPairOrPair(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.two_pair)
        self.assertEqual(output_hand.vals, [3,2,11])
        
    def test_getPair(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._5h, c._2d, c._3s, c._3h, c._6s, c._js, c._8c, c._7c])
        #output_hand = getTwoPairOrPair(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.pair)
        self.assertEqual(output_hand.vals, [3,11,8,7])

    def test_getStraight(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._5h, c._2d, c._3s, c._4h, c._6s, c._js, c._8c, c._7c])
        #output_hand = getStraight(classifyCardsByVal(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.straight)
        self.assertEqual(output_hand.vals, [8])

    def test_getStraightFlush(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._5d, c._2d, c._3d, c._4d, c._6d, c._js, c._8d, c._7d])
        #output_hand = getStraightFlushOrFlush(classifyCardsBySuit(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.straight_flush)
        self.assertEqual(output_hand.vals, [8])
    
    def test_getRoyalFlush(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._10d, c._jd, c._3d, c._4d, c._ad, c._js, c._kd, c._qd])
        #output_hand = getStraightFlushOrFlush(classifyCardsBySuit(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.royal_flush)
        self.assertEqual(output_hand.vals, [14])

    def test_getFlush(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._5d, c._2d, c._10d, c._4d, c._6d, c._js, c._9d, c._7d])
        #output_hand = getStraightFlushOrFlush(classifyCardsBySuit(cards))
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.flush)
        self.assertEqual(output_hand.vals, [10, 9, 7, 6, 5])

    def test_getHighCard(self):
        c = card.cards()
        cards = orderedCards.OrderedCards([c._5c, c._2s, c._10d, c._4c, c._6d, c._js, c._9h, c._7d])
        output_hand = evalHand(cards)
        self.assertEqual(output_hand.handType, HandType.high_card)
        self.assertEqual(output_hand.vals, [11,10, 9, 7, 6])

if __name__ == '__main__':
    unittest.main()
