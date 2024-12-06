import re
f = open("input.in.txt", "r")

num_rules = 0

num_dict = {}
for i in f.readlines():

    if(len(re.findall("\\|", i)) == 1):
        key, val  = i.split("|")
        val = int(val)
        key = int(key)

        # If key doesn't exist, make new entry
        if(key not in num_dict.keys()):
            num_dict[key] = []

        # Add each value
        if(val not in num_dict[key]):
            num_dict[key].append(val)

# We have a dictionary containing our dependencies

f.seek(0)

line_arr = []
total_counter = 0

def check_line_safe(array):
    unsafe1 = -1
    unsafe2 = -1

    safe = True
    # Loop over each permutation
    for i, val1 in enumerate(array):

        if (int(val1) not in num_dict.keys()):
            continue

        for j,val2 in enumerate(array):

            # If the value is in correct order
            if(int(val2) in num_dict[int(val1)] and int(j) > int(i)):
                pass
            # If the values are in the wrong order, return the pair that is unsafe
            elif(int(val2) in num_dict[int(val1)] and int(j) < int(i)):
                safe = False
                unsafe1 = int(i)
                unsafe2 = int(j)
    return safe, unsafe1, unsafe2

part1counter = 0
for line in f.readlines():

    safe = False
    array = []

    if(len(re.findall("\\,", line)) > 0):
        # Check if a line is safe
        array = line.split(",")
        safe, unsafe1, unsafe2 = check_line_safe(array)
        if(safe):
            part1counter += int((array[int(len(array)/2)]))
            pass

        # If the line isn't safe, we need to check what is wrong 
        # and swap
        elif(not safe):

            # WHile it doesn't work, try and fix it
            while not safe:
                safe, unsafe1, unsafe2 = check_line_safe(array)
                temp = array[unsafe1]
                array[unsafe1] = array[unsafe2]
                array[unsafe2] =temp 
            total_counter += int((array[int(len(array)/2)]))



print("Part 1 answer = ", part1counter)
print("Part 2 answer = ", total_counter)

