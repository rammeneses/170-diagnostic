# Raohael Andrei M. Meneses
# 2022-13211
# GH-2L

def print_state(state):
    
    for line in state:
        for num in line:
            print(num, end=" ")
        print()

test = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

print(test)

print_state(test)