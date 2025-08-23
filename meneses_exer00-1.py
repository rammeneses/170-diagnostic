# Raohael Andrei M. Meneses
# 2022-13211
# GH-2L

import os
from ctypes import windll

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

    

# Helper Variables
row = 1
col = 0

def get_z_loc(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            # print(i,j)
            if state[i][j] == 0:
                # print("z_loc", i,j)
                return (j,i)

# returns true if the current state is the goal state
def is_goal_state(state, goal):
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
        "w": "down",
        "W": "down",
        "a": "right",
        "A": "right",
        "s": "up",
        "S": "up",
        "d": "left",
        "D": "left"
    }
    # input verification
    if input in move_list.keys():
        # Out of bounds check
        # returns None 
        if move_list[input] == "down" and z_loc[row] == 2:
            return
        if move_list[input] == "up" and z_loc[row] == 0:
            return
        if move_list[input] == "right" and z_loc[col] == 2:
            return
        if move_list[input] == "left" and z_loc[col] == 0:
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
        case "up":
            swap_row = z_loc[row] - 1
            swap_col = z_loc[col]
        case "down":
            swap_row = z_loc[row] + 1
            swap_col = z_loc[col]
        case "left":
            swap_row = z_loc[row]
            swap_col = z_loc[col] - 1
        case "right":
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
    
    goal = [
        [1,2,3],
        [4,5,6],
        [7,8,0],
    ]
    # test state
    test = [
        [1,5,6],
        [2,3,0],
        [4,7,8],
    ]
    state = test
    z_loc = get_z_loc(state)
    solved = False
    # Main loop
    while True:
        # clear_terminal()
        print(header)
        print_state(state)
        if is_goal_state(state, goal): 
            if not solved:
                # Taken from the answer from
                # https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
                windll.user32.MessageBoxW(0, "You have solved the Puzzle!", "8-Puzzle", 0x00001040)
                solved = True
            else:
                print("SOLVED!")
        inp = read_input("\nInput: ").decode()
        # print(inp)
        # return
        match inp:
            case "1":
                from_file = get_file_input()
                state = from_file[0]
                z_loc = from_file[1]
                print_state(state)
                print(z_loc)
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