# Raphael Andrei M. Meneses
# 2022-13211
# GH-2L
# Exercise 1: BFS & DFS
# NOTE: I can't find the statement on the Responsible Use of AI in the Course Guide

import os
from ctypes import windll
import copy

if os.name == "nt":
    import msvcrt
else:
    import sys
    import tty
    import termios

# Clear Terminal taken from:
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Taken from:
# https://stackoverflow.com/questions/3523174/raw-input-without-pressing-enter
# https://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
def read_input(to_print):
    print(to_print)
    if os.name == 'nt':
        return msvcrt.getch()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def get_file_input():
    temp = []
    # print("in gfi")
    with open("input.txt", "r") as file:
        for line in file:
            temp3 = []
            temp2 = line.strip().split(";")
            for num in temp2:
                temp3.append(int(num))
            temp.append(temp3)
    z_loc = get_z_loc(temp)
    # while z_loc == None:
    #     z_loc = get_z_loc(temp)
    #     print(z_loc)
    return (temp, z_loc)

# Source: what I remember doing for my last 170 take TT
def verify_solvable(state):
    # put list of lists of ints into a single list
    temp = flatten_list(state)

    # Check and count inversions
    inversions = count_inversions(temp)

    # Evaluate the inversions
    # Even means solvable for 8-puzzle
    if inversions % 2 == 0:
        return True
    return False

def count_inversions(temp):
    # Check and count inversions
    inversions = 0
    for i in range(len(temp)):
        for j in range(len(temp)):
            if j <= i:
                continue
            if temp[i] > temp[j]:
                if temp[j] != 0:
                    inversions += 1
    return inversions

def flatten_list(state):
    # put list of lists of ints into a single list
    temp = []
    for line in state:
        for num in line:
            temp.append(num)
    return temp

# Helper Variables
row = 1
col = 0

def actions(state):
    legal_actions = []
    # checking is done UDRL
    temp = copy.deepcopy(state)
    z_loc = get_z_loc(temp)
    if z_loc[row] != 0:
        legal_actions.append("U")
    if z_loc[row] != 2:
        legal_actions.append("D")
    if z_loc[col] != 2:
        legal_actions.append("R")
    if z_loc[col] != 0:
        legal_actions.append("L")
    return legal_actions

def is_empty(list):
    if list == []:
        return True
    return False
    pass

# assumes moves are in bounds
# deepcopy idea taken from:
# https://www.geeksforgeeks.org/python/python-cloning-copying-list/
# NOTE: different from move_match that the player input does
#       but is basically the same
def move_result(state, action):
    temp = copy.deepcopy(state)
    print_state(temp)
    z_loc = get_z_loc(temp)

    match action:
        case "U":
            swap_row = z_loc[row] - 1
            swap_col = z_loc[col]
        case "D":
            swap_row = z_loc[row] + 1
            swap_col = z_loc[col]
        case "L":
            swap_row = z_loc[row]
            swap_col = z_loc[col] - 1
        case "R":
            swap_row = z_loc[row]
            swap_col = z_loc[col] + 1
    # swap proper
    new_z_loc = (swap_col, swap_row)
    # set the location of 0 to the number that it will swap with
    temp[z_loc[row]][z_loc[col]] = temp[new_z_loc[row]][new_z_loc[col]]
    # since we know that 0 will be moved
    temp[new_z_loc[row]][new_z_loc[col]] = 0
    
    # retun the new state after the move
    return temp

def actionCost(actions):
    return(len(actions))

def bfs(state):
    # frontier is formatted as
    # (state, path)
    frontier = [(copy.deepcopy(state), [])]
    # print(frontier)
    # explored is just a list of states, no paths
    explored = []
    while not is_empty(frontier):
        # basically dequeue
        current = frontier.pop(0)
        currentState = current[0]
        path = current[1]
        explored.append(currentState)
        # print(frontier)
        # print(f"currentState: {currentState}")
        if(is_goal_state(currentState)):
            return {
                "solution":path,
                "path_cost":actionCost(path),
                "explored":len(explored)
            }
        else:
            for a in actions(currentState):
                # print(f"a: {a}")
                result = move_result(currentState, a)
                p = path.copy()
                p.append(a)
                # print_state(result)
                if result not in explored and result not in frontier:
                    frontier.append((result, p))

def dfs(state):
    # frontier is formatted as
    # (state, path)
    frontier = [(copy.deepcopy(state), [])]
    # print(frontier)
    # explored is just a list of states
    explored = []
    while not is_empty(frontier):
        current = frontier.pop()
        currentState = current[0]
        path = current[1]
        explored.append(currentState)
        # print(frontier)
        # print(f"currentState: {currentState}")
        if(is_goal_state(currentState)):
            return {
                "solution":path,
                "path_cost":actionCost(path),
                "explored":len(explored)
            }
        else:
            for a in actions(currentState):
                # print(f"a: {a}")
                result = move_result(currentState, a)
                p = path.copy()
                p.append(a)
                # print_state(result)
                if result not in explored and result not in frontier:
                    frontier.append((result, p))
    pass

# assumes results_dict is from bfs or dfs
def parse_results(results_dict):
    # print(results_dict)
    # print(results_dict.get("solution"))
    decoded_list = []
    soln = ''.join(results_dict.get("solution"))
    for char in soln:
        match char:
            case 'U':
                decoded_list.append("S")
            case 'D':
                decoded_list.append("W")
            case 'R':
                decoded_list.append("A")
            case 'L':
                decoded_list.append("D")
    decoded = "".join(decoded_list)
    
    print(f"Solution: {soln}")
    print(f"Decoded: {decoded}")
    print(f"Cost: {results_dict.get("path_cost")}")
    print(f"Explored: {results_dict.get("explored")}\n")
    pass

def get_z_loc(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            # print(i,j)
            if state[i][j] == 0:
                # print("z_loc", i,j)
                return (j,i)

# returns true if the current state is the goal state
def is_goal_state(state, goal = [
        [1,2,3],
        [4,5,6],
        [7,8,0],
    ]):
    return True if state == goal else False

def print_state(state):
    for line in state:
        for num in line:
            print(num, end=" ")
        print()

def move_match(input, state, z_loc):
    # NOTE: The wasd keys represent movement of the NON-ZERO tiles
    #   The dictionary values represent the movement of the ZERO tile
    move_list = {
        "w": "D",
        "W": "D",
        "a": "R",
        "A": "R",
        "s": "U",
        "S": "U",
        "d": "L",
        "D": "L"
    }
    # input verification
    if input in move_list.keys():
        # Out of bounds check
        # returns None 
        if move_list[input] == "D" and z_loc[row] == 2:
            return
        if move_list[input] == "U" and z_loc[row] == 0:
            return
        if move_list[input] == "R" and z_loc[col] == 2:
            return
        if move_list[input] == "L" and z_loc[col] == 0:
            return
        
        # print(move_list[input])
        # Returns the return value of move()
        # which is a tuple of the new location of ZERO
        return move(move_list[input], state, z_loc)
    return
        
            
def move(input, state, z_loc):
    # print(input)
    # print(z_loc)
    # match case to set the coordinates for a swap
    match input:
        case "U":
            swap_row = z_loc[row] - 1
            swap_col = z_loc[col]
        case "D":
            swap_row = z_loc[row] + 1
            swap_col = z_loc[col]
        case "L":
            swap_row = z_loc[row]
            swap_col = z_loc[col] - 1
        case "R":
            swap_row = z_loc[row]
            swap_col = z_loc[col] + 1
    # swap proper
    new_z_loc = (swap_col, swap_row)
    # set the location of 0 to the number that it will swap with
    state[z_loc[row]][z_loc[col]] = state[new_z_loc[row]][new_z_loc[col]]
    # since we know that 0 will be moved
    state[new_z_loc[row]][new_z_loc[col]] = 0
    # return the updated location of zero
    return new_z_loc

def main():
    header = "8-Puzzle CLI\n" \
    "[w/a/s/d] Move\n" \
    "[1] Load input.txt\n" \
    "[0] Exit\n" 

    # test state
    # test = [
    #     [1,5,6],
    #     [2,3,0],
    #     [4,7,8],
    # ]
    test = [
        [2,3,0],
        [1,5,6],
        [4,7,8],
    ]
    state = test
    z_loc = get_z_loc(state)
    solved = False
    solvable = verify_solvable(state)
    search_results = None
    # print(solvable)
    # Main loop
    while True:
        # clear_terminal()
        print(header)
        if search_results:
            parse_results(search_results)
        print_state(state)
        if not solvable:
            print("NOT SOLVABLE!")
            windll.user32.MessageBoxW(0, "The Puzzle is not solvable!", "8-Puzzle", 0x00001010)

        if is_goal_state(state): 
            if not solved:
                # Taken from the answer from
                # https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
                windll.user32.MessageBoxW(0, "You have solved the Puzzle!", "8-Puzzle", 0x00001040)
                solved = True
            else:
                print("SOLVED!")
        try:
            inp = read_input("\nInput: ").decode()
        except:
            print("Invalid Input!")
            continue
        # print(inp)
        # return
        match inp:
            case "1":
                from_file = get_file_input()
                state = from_file[0]
                z_loc = from_file[1]
                solvable = verify_solvable(state)
            case "3":
                search_results = bfs(state)
            case "4":
                search_results = dfs(state)
            
            case "0":
                print("Goodbye!")
                break
        # break
        # store the return value of move_match()
        temp = move_match(inp, state, z_loc)
        # None represents an invalid move, Catch it here
        # Update z_loc only if we get a tuple as a return value
        if temp:
            z_loc = temp
    

main()