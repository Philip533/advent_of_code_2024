import re
import numpy as np
np.set_printoptions(threshold=np.inf,linewidth=np.inf)

f = open("input.in", "r")

pos = np.zeros((len(f.readlines()), 2))
f.seek(0)
velocity = np.zeros((len(f.readlines()), 2))
f.seek(0)
for index,i in enumerate(f.readlines()):

    match = (re.split("=",i))
    positions =  (re.findall("\\d+", match[1]))
    velocity1 =  (re.findall("-?\\d+", match[2]))
    pos[index,0:2] = [int(x) for x in positions]
    velocity[index,0:2] = [int(x) for x in velocity1]

time_total = 10000
tilesx = 101
tilesy = 103
midx = (tilesx-1)/2
midy = (tilesy-1)/2

pos_array = np.zeros((len(pos),2))
var_array = np.zeros(time_total)

# Each timestep
for t in range(1,time_total+1):

    # Reset the grid
    grid = np.zeros((tilesx,tilesy),dtype=int)

    # Loop over each robot
    for i,val in enumerate(pos):

        new_pos = np.add(pos[i], t*velocity[i,:])
        new_pos = np.mod(new_pos, (tilesx, tilesy))

        grid[int(new_pos[0]), int(new_pos[1])] += 1
        pos_array[i,:] = new_pos

    # Store variance along each direction
    var_array[t-1] = (np.var(pos_array[:,0])+ np.var(pos_array[:,1]))
    grid = grid.T
    safety_arr = np.zeros(4)

    # Part 1 answer
    if(t == 100):
        for i in range(tilesx):
            for j in range(tilesy):
                pass

                if(grid[j,i] != 0):

                    # Top left
                    if(0 <= i < midx and 0 <= j < midy):
                        safety_arr[0] += grid[j,i]
                    if(midx < i <= tilesx - 1 and 0 <= j < midy):
                        safety_arr[1] += grid[j,i]
                    if(0 <= i < midx and midy < j <= tilesy - 1):
                        safety_arr[2] += grid[j,i]
                    if(midx < i <= tilesx - 1 and midy < j <= tilesy - 1):
                        safety_arr[3] += grid[j,i]

        print("Part 1 answer = ", int(np.prod(safety_arr)))
print("Part 2 answer = ",np.argmin(var_array)+1)
