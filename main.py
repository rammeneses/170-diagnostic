# Raohael Andrei M. Meneses
# 2022-13211
# GH-2L

import os

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


# Helper Variables
x_axis = 0
y_axis = 1

def get_z_loc(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            # print(i,j)
            if state[i][j] == 0:
                # print("z_loc", i,j)
                return (j,i)

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
        if move_list[input] == "down" and z_loc[y_axis] == 2:
            return
        if move_list[input] == "up" and z_loc[y_axis] == 0:
            return
        if move_list[input] == "right" and z_loc[x_axis] == 2:
            return
        if move_list[input] == "left" and z_loc[x_axis] == 0:
            return
        
        # print(move_list[input])
        # Returns the return value of move()
        # which is a tuple of the new location of ZERO
        return move(move_list[input], state, z_loc)
        
            
def move(input, state, z_loc):
    # print(input)
    # print(z_loc)
    # match case to set the coordinates for a swap
    match input:
        case "up":
            swap_x = z_loc[x_axis]
            swap_y = z_loc[y_axis] - 1
        case "down":
            swap_x = z_loc[x_axis]
            swap_y = z_loc[y_axis] + 1
        case "left":
            swap_x = z_loc[x_axis] - 1
            swap_y = z_loc[y_axis]
        case "right":
            swap_x = z_loc[x_axis] + 1
            swap_y = z_loc[y_axis]
    # swap proper
    new_z_loc = (swap_x, swap_y)
    # set the location of 0 to the number that it will swap with
    state[z_loc[y_axis]][z_loc[x_axis]] = state[new_z_loc[y_axis]][new_z_loc[x_axis]]
    # since we know that 0 will be moved
    state[new_z_loc[y_axis]][new_z_loc[x_axis]] = 0
    # return the updated location of zero
    return new_z_loc

def main():
    header = "8-Puzzle CLI\n" \
    "[w/a/s/d] Move\n" \
    "[0] Exit\n"
    
    solved = [
        [1,2,3],
        [4,5,6],
        [7,8,0],
    ]
    # test state
    test = [
        [2,3,0],
        [1,5,6],
        [4,7,8],
    ]
    state = test
    z_loc = get_z_loc(state)
    # Main loop
    while True:
        clear_terminal()
        print(header)
        print_state(state)
        inp = read_input("\nMove? ").decode()
        # print(inp)
        # return
        if inp == "0":
            print("Goodbye!")
            break
        # store the return value of move_match()
        temp = move_match(inp, state, z_loc)
        # None represents an invalid move, Catch it here
        # Update z_loc only if we get a tuple as a return value
        if temp:
            z_loc = temp
    

main()