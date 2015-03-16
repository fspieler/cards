#/usr/bin/env python3

import itertools
import random
from src.card import *

class OrderedCards(object):
    def __init__(self,cards_list=None):
        if(cards_list is None):
            cards_list = []
        self.cards_list = cards_list

    def __str__(self):
        return('(' + ' '.join(map(str,self.cards_list)) + ')')

    def deal(self,num_cards, *users):
        for num in range(num_cards):
            for user in users:
                card = self.cards_list.pop(0)
                user.cards_list.append(card)

    def fromTop(self,num_cards):
        ret = OrderedCards([])
        self.deal(num_cards,ret)
        return ret

    def fromBottom(self,num_cards):
        ret = OrderedCards([])
        reverse = OrderedCards(self.cards_list[::-1])
        reverse.deal(num_cards,ret)
        self.cards_list = reverse.cards_list[::-1]
        return ret

    def toTop(self,*cards):
        self.cards_list = cards.extend(cards_list)

    def toBottom(self,*cards):
        self.cards_list.extend(cards)

    def list(self):
         return self.cards_list

def getDeck():
    deck = list(map(Card,itertools.product(range(2,15),range(0,4))))
    random.shuffle(deck)
    return OrderedCards(deck)

def printCards(list_of_cards):
    print(' '.join(map(str,list_of_cards)))

