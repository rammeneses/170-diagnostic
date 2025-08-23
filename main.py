# Raohael Andrei M. Meneses
# 2022-13211
# GH-2L
x_axis = 0
y_axis = 1

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
            return
        if move_list[input] == "up" and z_loc[y_axis] == 0:
            return
        if move_list[input] == "right" and z_loc[x_axis] == 2:
            return
        if move_list[input] == "left" and z_loc[x_axis] == 0:
            return
        
        # print(move_list[input])
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
    # update the location of zero
    return new_z_loc
    
            # # set the 0 to the number that it will swap with
            # state[z_loc[y_axis]][z_loc[x_axis]] = state[z_loc[y_axis] - 1][z_loc[x_axis]]
            # # since we know that 0 will be the only 
            # state[z_loc[y_axis] - 1][z_loc[x_axis]] = 0
            
            # print_state(state)

def main():
    test = [
        [1,2,3],
        [4,5,6],
        [7,8,0],
    ]
    z_loc = get_z_loc(test)
    # print(test[0][1])
    # return
    
    # print(test)

    while True:
        print_state(test)
        inp = input("Move? ")
        temp = move_match(inp, test, z_loc)
        if temp:
            z_loc = temp
    

main()