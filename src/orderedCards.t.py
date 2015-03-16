#/usr/bin/env python3

import unittest
from orderedCards import *

class TestOrderedCards(unittest.TestCase):

    def setUp(self):
        self.c = cards()


    def test_construction(self):
        c = self.c
        test_cards = [c.two_ofhearts, c.three_ofhearts, c.four_ofhearts]
        oc = OrderedCards(l_cards)
        self.assertEqual(test_cards, oc.cards_list)

    def test_normal_deal(self):
        c = self.c
        l_cards = [c.2h, card2, card3, card4]
        deck = OrderedCards(l_cards)
        dest = OrderedCards()
        deck.deal(2,dest)
        self.assertTrue(deck[0] == card3)
        self.assertTrue(deck[1] == card4)
        self.assertTrue(dest[0] == card1)
        self.assertTrue(dest[1] == card2)
        self.assertTrue(len(deck) == 2)
        self.assertTrue(len(dest) == 2)

if __name__ == '__main__':
    unittest.main()
