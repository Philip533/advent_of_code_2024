import numpy as np
import re

def part_one(matrix):

    counter = 0

    # Rows
    for i in matrix: 
        counter += len((re.findall("XMAS", ''.join(i))))
        counter += len((re.findall("SAMX", ''.join(i))))
        # print(re.findall("XMAS", ''.join(i)))
        # print(re.findall("SAMX", ''.join(i)))

    # Columns
    for i in np.transpose(matrix):
        # print(i)
        counter += len((re.findall("XMAS", ''.join(i))))
        counter += len((re.findall("SAMX", ''.join(i))))

    # Check each diagonal, using flip to check each direction
    for j in range(-matrix.size+1, matrix.size):
        diag1 = matrix.diagonal(offset=j)
        diag2 = np.flip(matrix,0).diagonal(offset=j)
        counter += len((re.findall("XMAS", ''.join(diag1))))
        counter += len((re.findall("SAMX", ''.join(diag1))))
        counter += len((re.findall("XMAS", ''.join(diag2))))
        counter += len((re.findall("SAMX", ''.join(diag2))))
    return counter

def part_two(matrix):
    counter = 0
    for i, val in enumerate(matrix):

        for j, val in enumerate(val):
            if(val == 'A'):
                # Edge cases
                if(j == 0):
                    continue
                elif(j == matrix.shape[0]-1):
                    continue
                if(i == 0):
                    continue
               if(i == matrix.shape[0]-1):
                    continue
                if((matrix[i-1][j-1] == "S") and (matrix[i+1][j+1] == "M")):
                    if((matrix[i+1][j-1] == "M") and (matrix[i-1][j+1] == "S")):
                        counter += 1
                    if((matrix[i+1][j-1] == "S") and (matrix[i-1][j+1] == "M")):
                        counter += 1
                if((matrix[i-1][j-1] == "M") and (matrix[i+1][j+1] == "S")):
                    if((matrix[i+1][j-1] == "M") and (matrix[i-1][j+1] == "S")):
                        counter += 1
                    if((matrix[i+1][j-1] == "S") and (matrix[i-1][j+1] == "M")):
                        counter += 1
    return counter

# Load in the file
f = np.loadtxt("input.in", dtype=str)

# Make a 2D array out of the input
big_arr = []
for i in f:
    list1 = (list(i))
    arr = np.array(list1)
    big_arr.append(arr)

matrix = (np.array(big_arr))

print("Part 1 answer = ", part_one(matrix))
print("Part 2 answer = ", part_two(matrix))


