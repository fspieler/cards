#/usr/bin/env python3

import unittest
import card

class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_construct_low_value(self):
        self.assertRaises(ValueError,card.Card,0,card.Suit.hearts) # 0 lower than 2 (lowest card)

    def test_construct_high_value(self):
        self.assertRaises(ValueError,card.Card,15,card.Suit.hearts) # 15 higher than Ace

    def test_construct_low_suit(self):
        self.assertRaises(ValueError,card.Card,2,-1) # 2 of impossible suit

    def test_construct_high_suit(self):
        self.assertRaises(ValueError,card.Card,2,4) # 2 of impossible suit

        
if __name__ == '__main__':
    unittest.main()
