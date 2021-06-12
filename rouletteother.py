# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:04:14 2020

@author: o0jl0
"""

#--ROULETTE--#
import random
funds = 100
red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
while True:
    n=random.randint(0,37)
    print('Welcome to Roulette! Place your bet.')
    print('Please pick a colour or a number')
    choice = input('Enter colour or number')
    if choice == 'colour':
        colour = input('Red = 1 Black = 2. Please input 1 or 2 ')
        if colour == '1' or colour == '2':
            bet = int(input('Enter the amount of chips you want to bet '))
            if bet > funds:
                print('Insufficient funds, your funds are:',funds)
                continue
            else:
                funds -= bet
            if colour == '1' and n in red:
                funds += bet*2
            if colour == '2' and n in black:
                funds += bet*2
    elif choice == 'number':
            number=int(input('Enter a number between 0 and 37'))
            if number >=0 and number <=37:
                bet = int(input('Enter the amount of chips you want to bet '))
                if bet > funds:
                    print('Insufficient funds, your funds are:',funds)
                else:
                    funds -= bet
            if number == n:
                funds += (bet + bet*35)
    else:
        print('No bets taken, please ensure input is correct')  
    print('The number is: ',n)
    print('Chips:',funds)
    new_game = input('Do you want to play again y/n: ')
    if funds <=0:
        print('Game over, you have no money!')
        break
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break