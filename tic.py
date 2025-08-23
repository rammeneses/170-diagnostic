# Raphael Andrei M. Meneses
# 2022-13211
# GH-2L
# NOTE: I can't find the statement on the Responsible Use of AI in the Course Guide

import os
from ctypes import windll

# Clear Terminal taken from:
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_state(state):
    for line in state:
        for char in line:
            print(char, end=" ")
        print()


# TODO: fix player turns
def manage_move(move, state, player_1_turn):
    row = move[0]
    col = move[1]

    # Getting the player type
    player = "O"
    if player_1_turn:
        player = "X"
    # Doing the move
    state[row][col] = player
    print("in mm")
    print_state(state)
    # inverting the player turn boolean
    return not player_1_turn
    pass

# TODO: add win conditions
def main():
    state = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]
    player_1_turn = True
    header = "Tic-Tac-Toe"
    # Main loop
    while True:
        print(header)
        if player_1_turn:
            print("Player 1's Turn(X): \n")
        else:
            print("Player 2's Turn(O): \n")
        print_state(state)
        move = [-1,-1]
        inp = manage_input(state)
        # breaking out of the loop and the program
        if inp == "q":
            print("Goodbye!")
            break
        # assigning the input as the move
        move = inp
        print(move)
        # validating the move
        valid_move = validate_move(move, state)
        if not valid_move:
            print("Invalid Move!")
            continue
        # managing and making the move
        manage_move(move, state, player_1_turn)

# returns false for out of bounds moves and moves on already filled spaces
# returns true otherwise
def validate_move(move, state):
    for num in move:
        print(num)
        if int(num) < 0 or int(num) > 2:
            return False
    if state[move[0]][move[1]] != "-":
        return False
    return True

def manage_input(state):
    temp1 = input("Move[0]: ")
    # pre-emptive return for quitting the program
    if temp1 == "q":
        return temp1
    temp2 = input("Move[1]: ")
    # pre-emptive return for quitting the program
    if temp2 == "q":
        return temp2
    # 
    move = (int(temp1), int(temp2))
    return move


main()