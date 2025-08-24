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

# is_end(self) function from last year's CMSC 170 tic-tac-toe lab
# adapted for my implementation of recursive tic-tac-toe
def check_winner(state):
    # Vertical win
    for i in range(0, 3):
        if (state[0][i] != '-' and
            state[0][i] == state[1][i] and
            state[1][i] == state[2][i]):
            return state[0][i]

    # Horizontal win
    for i in range(0, 3):
        if (state[i] == ['X', 'X', 'X']):
            return 'X'
        elif (state[i] == ['O', 'O', 'O']):
            return 'O'

    # Main diagonal win
    if (state[0][0] != '-' and
        state[0][0] == state[1][1] and
        state[0][0] == state[2][2]):
        return state[0][0]

    # Second diagonal win
    if (state[0][2] != '-' and
        state[0][2] == state[1][1] and
        state[0][2] == state[2][0]):
        return state[0][2]

    # Is the whole board full?
    for i in range(0, 3):
        for j in range(0, 3):
            # There's an empty field, we continue the game
            if (state[i][j] == '-'):
                return None
            
    # It's a tie!
    return '-'

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
    print("")

    winner = check_winner(state)
    # If there is a winner or a tie
    if winner:
        match winner:
            case "X":
                print(f"{winner} wins!")
                windll.user32.MessageBoxW(0, "Player 1(X) WINS!", "Tic-Tac-Toe", 0x00001040)
            case "O":
                print(f"{winner} wins!")
                windll.user32.MessageBoxW(0, "Player 2(O) WINS!", "Tic-Tac-Toe", 0x00001040)
            case "-":
                print("TIE!")
                windll.user32.MessageBoxW(0, "TIE!", "Tic-Tac-Toe", 0x00001040)
        return winner
    
    current_turn = "Player 1(X) turn" if player_1_turn else "Player 2(O) turn"
    print(current_turn)

    # 
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


def main():
    state = [
        # ["X","O","O"],
        # ["O","X","-"],
        # ["X","X","O"],
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]
    player_1_turn = True
    # Main loop
    tic_recursion(state, True, -2, 0, player_1_turn)
    return

main()