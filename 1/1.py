import numpy as np
f = open("input.in", "r")
data = np.loadtxt("input.in")
col1 = []
col2 = []

# Read into nicer arrays
for i in range(len(data)):
    col1.append(int(data[i][0]))
    col2.append(int(data[i][1]))

# Sort
sort1 = np.sort(col1)
sort2 = np.sort(col2)

counter = 0
print(sort2-sort1)
# Find the distances
for i in range(len(sort1)):
    counter += abs(sort1[i] - sort2[i])
print("Final sum for part 1 = ", counter)

counter_outer = 0
# Part 2
for i in range(len(sort1)):
    key = sort1[i]

    counter_inner = 0 
    # Loop over all the second column
    for j in range(len(sort2)):
        # Found a match
        if (sort2[j] == key):
            counter_inner += 1
    counter_outer += counter_inner*key
print("Final sum for part 2 = ", counter_outer)

