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

# returns false for moves on already filled spaces
# returns true otherwise
def validate_move(move, state):
    if state[move[0]][move[1]] != "-":
        return False
    return True

def tic_recursion(state, valid_move, move, loc, player_1_turn):
    header = "Tic-Tac-Toe"
    instructions = "[0/1/2] Moves\n" \
    "[b] Back to move(row)\n" \
    "[q] Quit\n"
    print(header)
    print(instructions)
    if not valid_move:
        print("Invalid move!")
    print_state(state)
    current_turn = "\nPlayer 1(X) turn" if player_1_turn else "\nPlayer 2(O) turn"
    print(current_turn)
    match loc:
        case 0:
            inp = input("Move(row): ")
            match inp:
                case "q":
                    print("Goodbye!")
                    return
                case "0" | "1" | "2":
                    tic_recursion(state, True, int(inp), 1, player_1_turn)
                case _:
                    tic_recursion(state, False, move, loc, player_1_turn)
        case 1:
            inp = input("Move(column): ")
            match inp:
                case "q":
                    print("Goodbye!")
                    return
                case "b":
                    tic_recursion(state, True, -2, 0, player_1_turn)
                case "0" | "1" | "2":
                    validated_move = validate_move((move, int(inp)), state)
                    if validated_move:
                        state[move][int(inp)] = "X" if player_1_turn else "O"
                        tic_recursion(state, True, int(inp), 0, not player_1_turn)
                    else:
                        tic_recursion(state, False, move, loc, player_1_turn)
                case _:
                    tic_recursion(state, False, move, loc, player_1_turn)
            pass
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
    tic_recursion(state, True, -2, 0, player_1_turn)
    return
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
main()
