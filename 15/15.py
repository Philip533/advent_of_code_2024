import numpy as np
from scipy.ndimage import shift

def part_one(grid):

    counter = 0
    for j in range(len(grid)):
        for i in range(len(grid)):

            if(grid[i,j] == 'O'):
                counter += 100*i + j
    return counter


f = open("input.in", "r")

matrix = []
grid = np.zeros((50,50), dtype=str)
for i in f.readlines():

    # print(i.split())
    if(not i.split()):
        break
    matrix.append(list(i.strip()))
grid=np.array(matrix)
f.seek(0)
instructions = []
for i in f.readlines():
    if(i[0] == '#'):
        continue
    if(not i.split()):
        continue

    for j, val in enumerate(i.strip()):
        instructions.append(val)

# print(grid)
# print(instructions)

def check_line(direction, grid, position):

    print("DIR", direction)
    if (direction == '^'):
        line = (grid[:position[0], position[1]])
        line = list(reversed(line))
    if (direction == '<'):
        line = (grid[position[0], :position[1]])
        line = list(reversed(line))
    if (direction == 'v'):
        line = (grid[position[0]+1:, position[1]])
    if (direction == '>'):
        line = (grid[position[0], position[1]+1:])
    return line

initial_coords = []
for j in range(len(grid)):
    for i in range(len(grid)):
        if(grid[i,j] == '@'):
            initial_coords = [i,j]

directions = {}
directions['^'] = [-1,0]
directions['<'] = [0,-1]
directions['v'] = [1,0]
directions['>'] = [0,1]
for direction in instructions:

    line = []

    # Find the line
    line = check_line(direction, grid, initial_coords)
    line = np.array(line)

    dir_vec = directions[direction]
    new_vec = np.add(initial_coords, dir_vec)

    for index, val in enumerate(line):

        # Find a space
        if(val == '.'):

            # If next to where we are, then just move
            if(index == 0):
                # Move @ along
                grid[initial_coords[0], initial_coords[1]] = '.'
                initial_coords = new_vec
                grid[initial_coords[0], initial_coords[1]] = '@'
                break
            else:
                flip = np.flip(line[:index+1])
                print(index)
                print(line[:index+1])
                print(flip)

                if (direction == '>'):
                    grid[initial_coords[0], initial_coords[1]] = '.'
                    grid[new_vec[0], new_vec[1]:new_vec[1]+index+1] = flip
                    initial_coords = new_vec
                    grid[initial_coords[0], initial_coords[1]] = '@'
                    break
                if (direction == 'v'):
                    grid[initial_coords[0], initial_coords[1]] = '.'
                    grid[new_vec[0]:new_vec[0]+index+1, new_vec[1]] = flip
                    initial_coords = new_vec
                    grid[initial_coords[0], initial_coords[1]] = '@'
                    break
                if (direction == '^'):
                    grid[initial_coords[0], initial_coords[1]] = '.'
                    grid[new_vec[0]-index:new_vec[0]+1, new_vec[1]] = line[:index+1]
                    initial_coords = new_vec
                    grid[initial_coords[0], initial_coords[1]] = '@'
                    break
                if (direction == '<'):
                    grid[initial_coords[0], initial_coords[1]] = '.'
                    grid[new_vec[0], new_vec[1]-index:new_vec[1]+1] = line[:index+1]
                    initial_coords = new_vec
                    grid[initial_coords[0], initial_coords[1]] = '@'
                    break
        elif(val == '#'):
            break
                 

    print(grid)

part1 = part_one(grid)
print(part1)
