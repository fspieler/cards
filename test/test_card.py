# /usr/bin/env python3

import unittest
from cards.card import Card, Suit


class TestCard(unittest.TestCase):

    def test_construct_low_value(self):
        self.assertRaises(
            ValueError, Card, 0, Suit.hearts
        )  # 0 lower than 2 (lowest card)

    def test_construct_high_value(self):
        self.assertRaises(ValueError, Card, 15, Suit.hearts)  # 15 higher than Ace

    def test_construct_low_suit(self):
        self.assertRaises(ValueError, Card, 2, -1)  # 2 of impossible suit

    def test_construct_high_suit(self):
        self.assertRaises(ValueError, Card, 2, 4)  # 2 of impossible suit
