#!/usr/bin/env python3

import unittest
from cards.card import all_cards
from cards.ordered_cards import *

c = all_cards()


class TestOrderedCards(unittest.TestCase):

    def test_construction(self):
        test_cards = [c._2h, c._3h, c._4h]
        oc = OrderedCards(test_cards)
        self.assertEqual(test_cards, oc.cards_list)

    def test_normal_deal(self):
        card1 = c._2h
        card2 = c._as
        card3 = c._jd
        card4 = c._5c
        l_cards = [card1, card2, card3, card4]
        deck = OrderedCards(l_cards)
        dest = OrderedCards()
        deck.deal(2, dest)
        self.assertTrue(deck[0] == card3)
        self.assertTrue(deck[1] == card4)
        self.assertTrue(dest[0] == card1)
        self.assertTrue(dest[1] == card2)
        self.assertTrue(len(deck) == 2)
        self.assertTrue(len(dest) == 2)


if __name__ == "__main__":
    unittest.main()
