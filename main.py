# Raohael Andrei M. Meneses
# 2022-13211
# GH-2L

def get_z_loc(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return (i,j)

def print_state(state):
    for line in state:
        for num in line:
            print(num, end=" ")
        print()

def move_match(input, state, z_loc):
    x_axis = 0
    y_axis = 1
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
    if input in move_list.keys():
        if move_list[input] == "down" and z_loc[y_axis] == 2:
            return "Out of Bounds"
        if move_list[input] == "up" and z_loc[y_axis] == 0:
            return "Out of Bounds"
        if move_list[input] == "right" and z_loc[x_axis] == 2:
            return "Out of Bounds"
        if move_list[input] == "left" and z_loc[x_axis] == 0:
            return "Out of Bounds"
        
        # print(move_list[input])
        move(move_list[input], state, z_loc)
            
def move(input, state, z_loc):
    print(input)
    print(z_loc)
    print_state(state)

test = [
    [1,2,3],
    [4,5,6],
    [7,8,0],
]

# print(test)

# print_state(test)

# move_match(input("Move? "), test)
print(get_z_loc(test))