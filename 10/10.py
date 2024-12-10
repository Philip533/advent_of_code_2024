import numpy as np
import sys

f = np.loadtxt("input.in", dtype=str)

big_arr = []
for i in f:
    list1 = list(i)
    arr = np.array(list1)
    big_arr.append(arr)
grid = np.array(big_arr, dtype=int)
print(grid)


zeroes = []
for i in range(len(grid)):
    for j in range(len(grid)):
        if(grid[i,j] == 0):
            zeroes.append([i,j])

counter = 0
for i in zeroes:
    print(i)

    coords = [i]
    elevation = 0
    
    while elevation < 9:

        temp_coords = []
        for k in coords:

            print(k, elevation, "K")
            if (k[0]-1 < 0):
                pass
            else:
                if (grid[k[0]-1,k[1]] - grid[k[0], k[1]] == 1):
                    temp_coords.append([k[0]-1, k[1]])
            if (k[0]+1 > len(grid)-1):
                pass
            else:
                if (grid[k[0]+1,k[1]] - grid[k[0], k[1]] == 1):
                    temp_coords.append([k[0]+1, k[1]])
            if (k[1]-1 < 0):
                pass 
            else:
                if (grid[k[0],k[1]-1] - grid[k[0], k[1]] == 1):
                    temp_coords.append([k[0], k[1]-1])
            if (k[1]+1 > len(grid)-1):
                pass 
            else:
                if (grid[k[0],k[1]+1] - grid[k[0], k[1]] == 1):
                    temp_coords.append([k[0], k[1]+1])

            # Up
            # Down
            # Right
            # Left

        if(temp_coords == []):
            break
        elevation += 1
        coords = temp_coords

    coords = [(c[0],c[1]) for c in coords]
    counter += len((coords))

print(counter) 

