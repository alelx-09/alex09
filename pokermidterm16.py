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
       if ranks.count(card) == 2:
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
            
   
def full_house():
    if pair() and three_of_akind():
        print("you have a full house")
        return True
        
def flush():
    for ranks in list:
        card.index["J"] = 11 