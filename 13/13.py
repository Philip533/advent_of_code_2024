import numpy as np
import re
f = open("input.in", "r")
count = 0
matrix = np.zeros((2,2))
target = np.zeros(2, dtype=int)
part1 = 0
for i in f.readlines():

    complete = False
    if(not i.strip()):
        continue
    # First line

    if(re.search("A", i)):
        # Search for the two numbers
        vals = (re.findall("\\d+\\d+",i))
        vals[0] = int(vals[0])
        vals[1] = int(vals[1])
        matrix[0,:] = vals

    if(re.search("B\\:", i)):
        # Search for the two numbers
        vals = (re.findall("\\d+\\d+",i))
        vals[0] = int(vals[0])
        vals[1] = int(vals[1])
        matrix[1,:] = vals

    if(re.search("Prize", i)):
        # Search for the two numbers
        vals = (re.findall("\\d+\\d+",i))
        vals[0] = int(vals[0])+10000000000000
        vals[1] = int(vals[1])+10000000000000
        target = vals
        complete = True

    if (complete):
        matrix = matrix.T
        a = np.array([matrix[0,:], matrix[1,:]])
        b = target
        solution = np.linalg.solve(a,b)

        if(np.isclose(solution[0], round(solution[0]),rtol=1e-15)):
            if(np.isclose(solution[1], round(solution[1]),rtol=1e-15)):
                   part1 += 3*round(solution[0]) + round(solution[1])

print(part1)

