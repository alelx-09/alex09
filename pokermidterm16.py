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
            
            
            

def three_of_a_kind(rank_list):
    rank_list.sort()
    for card in rank_list:
        if rank_list.count(card)== 3
        return 3
    retun 0
            
        
def four_of_akind(rank_list):
    for card in ranks:
        if ranks.count(card) == 4:
           return 7 
        return 0
            
def five_of_akind():
    for card in ranks:
        if ranks.count(card) ==5:
            return True
        elif: 
            return False
            
   
def full_house():
    if pair() and three_of_akind(rank_list):
      if find_pairs(rank_list) == 2 and three_of_a_kind(rank_list):
          return 6 
         return 0
        
        
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
    
def straight_flush(rank_list, hand):
    if straight(rank_list) and flush(hand):
        return 8
    return 0

def evaluate_hand(rank_list, hand):
    best_hand = find_pairs(rank_list)
    best_hand = 3 if three_of_a_kind(ranks_list)> best_hand else best hand
    best_hand = 4 if straight(rank_list) > best_hand else best_hand
    best_hand = 5 if flush(hand)>best_hand else best_hand
    best_hand = 6 if full_house(rank_list) > best_hand else best_hand
    best_hand = 7 if foour_of_a_kind(rank_list) best_hand > best_hand
    best_hand = 8 if straight_flush(rank_list,hand) > best_hand else best_hand
    
        
        
if__name__==__"main"__:
    deck = pokerDeck()
    shufle(deck)
    hand = deal_hand(deck)
    ranks_list = get_ranks(hand)
    evaluate_hand(rank_list,hand)

        
