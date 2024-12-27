import numpy as np
from itertools import product
with open('input.in') as f:
   num_lines = sum(1 for _ in f)

f = open("input.in")

num_blocks = int(num_lines/7)
block_count = 0
count = 0
big_lock_arr = []
big_key_arr = []
while True:
    lock = False
    # print(block_count, num_blocks)
    if(block_count == 500):
        break
    blank = False
    lines = []
    for i in range(7):
        count += 1
        line = f.readline().strip()
        if(i == 0 and line == '#####'):
            lock = True
        if(not line):
            blank = True
            break
        else:
            lines.append(list(line))
    if(blank):
        continue
    else:
        block_count += 1

    full_grid = (np.array(lines))

    key_arr = []
    block_arr = []
    for k in range(full_grid.shape[1]):

        sliced = full_grid[:,k]

        key_count = 0
        for m in sliced:
            if(m == '#'):
                key_count += 1
        key_arr.append(key_count-1)

    if(lock):
        big_lock_arr.append(key_arr)
    else:
        big_key_arr.append(key_arr)
    # print(big_key_arr)
    # print(big_lock_arr)

# print("HERE")
good_count = 0
for key in big_key_arr:
    for lock in big_lock_arr:
        bad = False
        for i in range(5):
            # print(abs(lock[i]- key[i]))
            if(abs(lock[i]+ key[i]) > 5):
                # print(abs(lock[i] + key[i]))
                # print("HERE")
                bad = True
        if(not bad):
            good_count += 1

            # print(lock, key)
print("Part 1 = ",good_count)
