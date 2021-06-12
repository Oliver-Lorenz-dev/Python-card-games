# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:47:12 2020

@author: o0jl0
"""

import random

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}

playing = True


class Card:
    
    def __init__(self,suit,rank, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                for rank, value in values.items():
                    self.deck.append(Card(suit,rank,value))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += ' \n ' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    
    def __init__(self):
        self.cards = []
        self.values = []
        
    def add_card(self,card):
        self.cards.append(card)
        self.values.append(card.value)
    def __str__(self):
        return '{}'.format(self.value) 
        
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter number of chips to bet: '))
        except ValueError:
            print('Please input an integer')
        else:
            if chips.bet > chips.total:
                print('You do not have enough chips')
            else:
                break
def show_all(player,dealer):
    global Player_Same_Suit
    global Dealer_Same_Suit
    player_suit_list=[]
    dealer_suit_list=[]
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    for card in player.cards:
        player_suit_list.append(card.suit)
    for card in dealer.cards:
        dealer_suit_list.append(card.suit)
    if player_suit_list[0] == player_suit_list[1] == player_suit_list[2]:
       Player_Same_Suit = True
        
    if dealer_suit_list[0] == dealer_suit_list[1] == dealer_suit_list[2]:
        Dealer_Same_Suit = True
        
while True:
    print('Welcome to 3 card poker!')
    Player_Straight_Flush = False
    Dealer_Straight_Flush = False
    Player_Straight = False
    Dealer_Straight = False
    Player_Three_of_a_kind = False
    Dealer_Three_of_a_kind = False
    Player_Flush = False
    Dealer_Flush = False
    Player_Pair = False
    Dealer_Pair = False
    Player_Same_Suit = False
    Dealer_Same_Suit = False
    Player_Win = False
    Dealer_Win = False
    Tie = False
        
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    show_all(player_hand,dealer_hand)
    hand = player_hand.values
    hand.sort()
    hand2 = dealer_hand.values
    hand2.sort()
    
    ##conditions##
    ##Player
    if hand[0]+1 == hand[1] and hand[1]+1 == hand[2] and Player_Same_Suit:
        Player_Straight_Flush = True
        print('player straight flush')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    elif hand[0] == hand[1] and hand [1] == hand[2]:
        Player_Three_of_a_kind = True
        print('player 3 of a kind')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    elif hand[0]+1 == hand[1] and hand[1]+1 == hand[2]:
        Player_Straight = True
        print('player straight')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    elif Player_Same_Suit:
        Player_Flush = True
        print('player flush')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    elif hand[0] == hand[1] or hand[1] == hand[2]:
        Player_Pair = True
        print('player pair')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    else:
        Player_HighCard = True
        print('player high card')
        hand.sort(reverse = True)
        High_Card_Player = hand[0]
        print('player High card: ',High_Card_Player)
    ##Dealer
    if hand2[0]+1 == hand2[1] and hand2[1]+1 == hand2[2] and Dealer_Same_Suit:
        Dealer_Straight_Flush = True
        print('dealer straight flush')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    elif hand2[0] == hand2[1] and hand2[1] == hand2[2]:
        Dealer_Three_of_a_kind = True
        print('dealer 3 of a kind')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    elif hand2[0]+1 == hand2[1] and hand2[1]+1 == hand2[2]:
        Dealer_Straight = True
        print('dealer straight')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    elif Dealer_Same_Suit:
        Dealer_Flush = True
        print('dealer flush')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    elif hand2[0] == hand2[1] or hand2[1] == hand2[2]:
        Dealer_Pair = True
        print('dealer pair')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    else:
        Dealer_HighCard = True
        print('dealer high card')
        hand2.sort(reverse = True)
        High_Card_Dealer = hand2[0]
        print('dealer High Card: ',High_Card_Dealer)
    
    hand2.sort(reverse = True)
    High_Card_Dealer = hand2[0]
    hand.sort(reverse = True)
    High_Card_Player = hand[0]
    ##Comparison
    if Player_Straight_Flush and Dealer_Straight_Flush:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins! - straight flush of higher card than dealer straight flush')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer has higher straight flush -you lose')
    elif Player_Straight_Flush:
        Player_Win = True
        print ('player wins! - straight flush')
    elif Dealer_Straight_Flush:
        Player_Win = False
        print('dealer straight flush - you lose!')
    elif Player_Three_of_a_kind and Dealer_Three_of_a_kind:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins, higher three of a kind than dealer!')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer has higher three of a kind - you lose')
    elif Player_Three_of_a_kind:
        Player_Win = True
        print('player wins! three of a kind')
    elif Dealer_Three_of_a_kind:
        Player_Win = False
        print('dealer three of a kind! - you lose')
    elif Player_Straight and Dealer_Straight:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins! straight of higher card than dealer straight!')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer has higher straight - you lose')
    elif Player_Straight:
        Player_Win = True
        print('player wins! Straight!')
    elif Dealer_Straight:
        Player_Win = False
        print('dealer wins - dealer straight')
    elif Player_Flush and Dealer_Flush:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins! player flush of higher card than dealer flush')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer has higher flush you lose')
    elif Player_Flush:
        Player_Win = True
        print('Player wins - flush')
    elif Dealer_Flush:
        Player_Win = False
        print ('dealer wins - dealer flush')
    elif Player_Pair and Dealer_Pair:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins! - higher pair than dealer!')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer wins! Higher pair than player!')
    elif Player_Pair:
        Player_Win = True
        print('player wins! pair!')
    elif Dealer_Pair:
        Player_Win = False
        print('dealer wins - pair!')
    else:
        if High_Card_Player > High_Card_Dealer:
            Player_Win = True
            print('player wins - high card!')
        elif High_Card_Player == High_Card_Dealer:
            Tie = True
            print('tie')
        else:
            Player_Win = False
            print('dealer wins - high card!')
    if Player_Win:
        Chips.win_bet(player_chips)
    elif Tie:
        pass
    else:
        Chips.lose_bet(player_chips)
    print('Numer of chips:',player_chips.total)
    
    break

