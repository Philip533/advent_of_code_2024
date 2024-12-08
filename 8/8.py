import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
# Returns displacement vector
def displacement(pos1, pos2):
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    return [x,y]

def find_antinodes(matrix, is_part1):
    new_mat = np.copy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # print(matrix[i,j])

            p1 = np.array([i,j])
            # Found non dot
            if(matrix[i,j] != "."):

                for k in range(len(matrix)):
                    for l in range(len(matrix)):
                        p2 = np.array([k,l])
                        if(matrix[k,l] == matrix[i,j]):

                            if(k == i and j == l):
                                continue

                            p1_new = np.copy(p1)
                            disp = np.array(displacement(p1, p2))

                            if (is_part1):
                                p1_new = np.subtract(p1_new,disp)
                                if(p1_new[0] < 0 or p1_new[0] > len(matrix)-1):
                                    break
                                elif(p1_new[1] < 0 or p1_new[1] > len(matrix)-1):
                                    break
                                else:
                                    new_mat[p1_new[0], p1_new[1]] = '#'

                            # Keep subtracting
                            while not is_part1:
                                new_mat[i,j] = '#'
                                p1_new = np.subtract(p1_new,disp)

                                if(is_part1): 
                                    break
                                if(p1_new[0] < 0 or p1_new[0] > len(matrix)-1):
                                    break
                                elif(p1_new[1] < 0 or p1_new[1] > len(matrix)-1):
                                    break
                                else:
                                    new_mat[p1_new[0], p1_new[1]] = '#'
    return new_mat

# Read file into 2d array
f = np.loadtxt("input.in", dtype=str)
big_arr = []
for i in f:
    list1 = (list(i))
    arr = np.array(list1)
    big_arr.append(arr)

matrix = (np.array(big_arr))
counter = 0

new_mat = find_antinodes(matrix, True)
for i in range(len(new_mat)):
    for j in range(len(new_mat)):
        if(new_mat[i,j] == '#'):
            counter += 1
print("Part 1 answer = ", counter)
counter = 0
new_mat = find_antinodes(matrix, False)
for i in range(len(new_mat)):
    for j in range(len(new_mat)):
        if(new_mat[i,j] == '#'):
            counter += 1
print("Part 2 answer = ",counter)

