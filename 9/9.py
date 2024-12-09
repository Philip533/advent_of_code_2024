import numpy as np

def expand_line(line):

    block_sizes = []
    dot_sizes = []
    new_list = []
    counter = 0
    for index, value in enumerate(line):

        # File on even
        if(index % 2 == 0):
            block_sizes.append(int(value))
            for j in range(int(value)):
                new_list.append(counter)
            counter += 1
        elif(index % 2 == 1):
            dot_sizes.append(int(value))
            for j in range(int(value)):
                new_list.append(".")
    return new_list, block_sizes, dot_sizes

f = open("input.in", "r")

blocks = []
for i in f:
    line = list(i)

expanded, blocks, dots = expand_line(line)
expanded_orig, blocks, dots = expand_line(line)

dot_list = []
defragged = expanded

for index, val in enumerate(expanded):
    if(val == '.'):
        dot_list.append(index)

# print(dot_list)
dot_counter = 0
block_counter = len(blocks) - 1
# Now loop backwards over the expanded list
for j in range(len(expanded)-1,-1, -1):

    # Skip if looking at dot
    if (expanded[j] == '.'):
        continue

    # If to the left of dots, move on
    if (j <= dot_list[dot_counter]):
        break

    # Swap the numbers 
    defragged[dot_list[dot_counter]] = expanded[j]
    defragged[j] = '.'
    dot_counter += 1

# Now add up
counter = 0
print(defragged)
# print(expanded_orig)
for index, val in enumerate(defragged):
    if (val == '.'):
        continue
    counter += index*val
print(counter)
