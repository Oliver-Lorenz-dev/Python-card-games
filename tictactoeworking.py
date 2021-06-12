# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:14:30 2020

@author: o0jl0
"""

import random

def display_board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 please choose X or O: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 ='X'
    return(player1,player2)
def player2_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 2 please choose X or O: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 ='X'
    return(player1,player2)
def place_marker(board, marker, position):
    if marker == 'X' or marker == 'O' and position >= 1 and position <= 9:
        board [position] = marker
    else:
        print('Incorrect input')
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    else:
        return False
def choose_first():
    r1=random.randint(1, 2)
    if r1 == 1:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    replay = ''
    replay = input('Do you want to play again? Enter YES or NO')
    if replay == "YES":
        return True
    elif replay == "NO":
        return False
    else:
        print('Incorrect input')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
            
