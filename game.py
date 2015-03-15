#!/usr/bin/python3

import itertools, random 

# create deck
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club'])) 
# shuffle deck
random.shuffle(deck) 
# draw five cards 
print("You got:") 
for i in range(5): 
    print(deck[i][0], "of", deck[i][1])

