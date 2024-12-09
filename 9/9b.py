import numpy as np

def expand_line(line):

    block_sizes = []
    dot_sizes = []
    new_list = []
    counter = 0
    index_counter = 0
    dot_counter = 0
    for index, value in enumerate(line):


        # File on even
        if(index % 2 == 0):
            block_sizes.append([index_counter, int(value)])
            for j in range(int(value)):
                new_list.append(counter)
                index_counter += 1
                dot_counter += 1
            counter += 1
        elif(index % 2 == 1):
            # block_sizes.append(-int(value))
            dot_sizes.append([dot_counter,int(value)])
            for j in range(int(value)):
                new_list.append(".")
                index_counter += 1
                dot_counter += 1
    return new_list, block_sizes, dot_sizes

f = open("input.in", "r")

blocks = []
for i in f:
    line = list(i)
    # line = line[:-1]

expanded, blocks, dots = expand_line(line)
expanded_orig, blocks, dots = expand_line(line)

dot_list = []
defragged = expanded

blocks.reverse()

# Loop over all the files
for i in blocks:

    # Loop over the empty spaces
    for j in range(len(dots)):

        # If no spaces then move to next dots
        if(dots[j][0] == 0):
            continue

        # If dots to the right then skip
        if(i[0] <= dots[j][0]):
            continue

        # If space fill it in
        if (i[1] <= dots[j][1]):

            # Move the numbers into the gap
            defragged[dots[j][0]:dots[j][0]+i[1]] = expanded_orig[i[0]:i[0]+i[1]]

            # Shift the location of the dots
            dots[j][1] = dots[j][1] - i[1]
            dots[j][0] = dots[j][0] + i[1]

            # Fill in dots where numbers have moved from
            for k in range(i[1]):
                defragged[i[0]+k] = '.'
            # Move on to next loop
            break

# Now add up
counter = 0
for index, val in enumerate(defragged):
    if (val == '.'):
        continue
    counter += index*val
print(counter)
