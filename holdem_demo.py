#!/usr/bin/env python3

from cards.ordered_cards import get_deck, OrderedCards
from cards.poker_hands import eval_hand, holdem_monte_carlo

deck = get_deck()


fred = OrderedCards()
al = OrderedCards()
community = OrderedCards()

def print_odds(deck, community, al, fred):
    odds = holdem_monte_carlo(deck, community, 10000, al, fred)
    print(f"Odds: Al: {odds[0]:.0%}, Fred: {odds[1]:.0%}")
    print("")

deck.deal(2, al, fred)
al.sort()
fred.sort()
print("Al's hand: " + str(al))
print("Fred's hand: " + str(fred))
print_odds(deck, community, al, fred)
deck.deal(3,community)
print("Flop: " + str(community))
print_odds(deck, community, al, fred)
deck.deal(1,community)
print("Turn: " + str(community))
print_odds(deck, community, al, fred)
deck.deal(1,community)
print("River: " + str(community))
fred += community
al += community
alHand = eval_hand(al)
fredHand = eval_hand(fred)
print("Al's best hand: " + str(alHand))
print("Fred's best hand: " + str(fredHand))
if fredHand > alHand:
    print("Fred wins!")
elif alHand > fredHand:
    print("Al wins!")
else:
    print("Push!")
