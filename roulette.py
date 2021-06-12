# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:57:25 2020

@author: o0jl0
"""

#--ROULETTE--#
import random

red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
n=random.randint(0,37)


if n in red:
    print('red')
elif n in black:
    print('black')
else:
    print('green')
class Chips:
    
    def __init__(self):
        self.funds = 100
        self.bet = 0
        
    def win_colour(self):
        self.funds += self.bet
    
    def lose_bet(self):
        self.funds -= self.bet
    
    def win_number(self):
        self.funds += self.bet*35
    
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter number of chips to bet: '))
        except ValueError:
            print('Please input an integer')
        else:
            if chips.bet > chips.funds:
                print('You do not have enough chips')
            else:
                break
while True:
    print('Welcome to Roulette! Place your bet.')
    player_chips = Chips()
    
    print('Please pick a colour and/or a number')
    
    colour = input('Pick red or black ')
    if colour == 'red' or colour =='black':
        take_bet(player_chips)
    else:
        print('No bet on red or black taken')
        
    number=int(input('Enter a number between 0 and 37 '))
    if number >=0 and number <=37:
        take_bet(player_chips)
    else:
        print('No bet on numbers taken')
        
    
    n=30#random.randint(0,37)
    print('The number is: ',n)
    if number == n:
        player_chips.win_number()
    if colour == 'red' and number in red:
        player_chips.win_colour()
    elif colour == 'black' and number in black:
        player_chips.win_colour()
    else:
        player_chips.lose_bet()
    print('Chips:',player_chips.funds)
    new_game = input('Do you want to play again y/n: ')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break