import numpy as np
import itertools
f = open("input.in", "r")

length1 = (len(f.readlines()))
is_good = np.zeros(length1)
result_arr = np.zeros(length1)
f.seek(0)
for index1,i in enumerate(f.readlines()):

    # All the info we need
    result = int(i.split(":")[0])
    result_arr[index1] = result
    array = (i.split(":")[1])
    array1 = array.split(" ")
    nums = (array1[1:])
    nums = np.array(nums,dtype=int)

    length = len(nums)

    # List of permutations of the three operations
    op_arr = (list(itertools.product(range(3), repeat=length-1)))

    # Loop over each permutation
    for k in op_arr:

        # Start at the first number
        sum = nums[0]

        # Skip if the line has already been found as correct
        if(is_good[index1] == 1):
            break

        # Loop over each operation
        for index2, j in enumerate(k):

            # Addition
            if (j == 0):
                sum += nums[index2+1]
            # Multiplication
            elif (j == 1):
                sum *= nums[index2+1]
            # Concatenation
            elif (j == 2):
                sum = int(str(sum) + str(nums[index2+1]))
        # Track the line being safe
        if(int(sum) == result):
            is_good[index1] = 1

count = 0
# Count up everything
for i in range(length1):
    if(is_good[i] == 1):
        count += int((result_arr[i]))

print("Part 2 answer = ", count)
