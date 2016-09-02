# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:23:02 2016

@author: a.estrella2
"""
from pokerdeck import *
from random import choice, shuffle


deck = PokerDeck()
    
shuffle(deck)

myCard = choice(deck)

card = Card(rank = "k", suit ="♥")

hand = []

def deal_hand():   
    while len(hand) <5:
        card = choice(deck)
        hand.append(card)
        deck.remove(card)
    return hand
    
for _ in range(5):
    hand.append(choice(deck)) 
    
for card in hand:
    print(card)
            
def pair():
    for card in ranks:
       if ranks.count(card) == 2 and card not in pairs:
            print(card + "you have a pair")
            return True
            
            
            

def three_of_akind():
    for card in ranks:
        if ranks.count(card) == 3:
            print(card + "you have a pair")
            print("you have three of a kind")
            return True
            
        
def four_of_akind():
    for card in ranks:
        if ranks.count(card) == 4:
           print("you have four of a kind")
           return True
            
def five_of_akind():
    for card in ranks:
        if ranks.count(card) ==5:
            return True
        elif: 
            return False
            
   
def full_house():
    if pair() and three_of_akind():
        print("you have a full house")
        return True
        
        
def straight(len(ranks)):
    if ranks[i] == "j"
        ranks[i] == 11
    elif ranks[i]== "Q"
        ranks[i] == 12
    elif ranks[i] == "K"
        ranks[i] == 13
    elif ranks[i] == "A"
        ranks[i] == 14
    else:
        ranks[i] = int(ranks[i])
    if (int(ranks[4]) - ranks[0] ==4):
        return True
    else: 
        return False
        
def flush():
    if mysuits.count = 5:
        print("you have a flush")
        
        
        
if__name__==__"main"__:
    deck = pokerDeck()
    hand = []
    hand deal_hand(deck)
    ranks = []

        
