#!/usr/bin/env python3

import itertools
import copy
import random
from .card import *

class OrderedCards(object):
    def __init__(self,cards_list=None):
        if(cards_list is None):
            cards_list = []
        self.cards_list = cards_list

    def __str__(self):
        return('(' + ' '.join(map(str,self.cards_list)) + ')')

    def __repr__(self):
        return self.__str__()

    def deal(self,num_cards, *users):
        for num in range(num_cards):
            for user in users:
                card = self.cards_list.pop(0)
                user.cards_list.append(card)

    def fromTop(self,num_cards=1):
        ret = OrderedCards([])
        self.deal(num_cards,ret)
        if num_cards == 1:
            return ret.list()[0]
        return ret

    def fromBottom(self,num_cards=1):
        ret = OrderedCards([])
        reverse = OrderedCards(self.cards_list[::-1])
        reverse.deal(num_cards,ret)
        self.cards_list = reverse.cards_list[::-1]
        if num_cards == 1:
            return ret.list()[0]
        return ret

    def toTop(self,*cards):
        for idx,card in enumerate(cards):
            self.cards_list.insert(idx,card)

    def toBottom(self,*cards):
        for card in cards:
            self.cards_list.append(card)

    def list(self):
        return self.cards_list

    def __len__(self):
        return len(self.cards_list)

    def __getitem__(self,index):
        if isinstance(index,slice):
            return OrderedCards(self.cards_list[:][slice])
        return self.cards_list[index]

    def __copy__(self):
        return OrderedCards(list(self.cards_list))

    def __deepcopy__(self,memo):
        return OrderedCards(list(self.cards_list))

    def __add__(self, other):
        if type(other) is OrderedCards:
            ret = copy.copy(self)
            for c in other.cards_list:
                ret.toBottom(c)
        elif type(other) is Card:
            ret = copy.copy(self)
            ret.toBottom(other)
        else:
            raise TypeError("Expecting OrderedCards or Card; got {}".format(type(other)))
        return ret

    def __radd__(self, other):
        if type(other) is OrderedCards:
            ret = copy.copy(self)
            for c in other.cards_list:
                ret.toTop(c)
        elif type(other) is Card:
            ret = copy.copy(self)
            ret.toTop(other)
        else:
            raise TypeError("Expecting OrderedCards or Card; got {}".format(type(other)))
        return ret

    def __iadd__(self, other):
        if type(other) is OrderedCards:
            for c in other.cards_list:
                self.toTop(c)
        elif type(other) is Card:
            self.toTop(other)
        else:
            raise TypeError("Expecting OrderedCards or Card; got {}".format(type(other)))
        return self


def getDeck():
    deck = list(map(Card,itertools.product(range(2,15),range(0,4))))
    random.shuffle(deck)
    return OrderedCards(deck)

def printCards(list_of_cards):
    print(' '.join(map(str,list_of_cards)))

