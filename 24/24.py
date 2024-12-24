import numpy as np

f = open("input.in")

initial_dict = {}
operations = []
for i in f.readlines():
    if(not i.split()):
        continue
    # print(i)
    if(i[3] == ":"):
        x,y = (i.strip().split(":"))
        initial_dict[x] = y
    else:
        split = (i.split())
        del split[3]
        # print(split)
        operations.append(split)
count = 0
skipped = True 
while skipped:
    skipped = False
    for index, val in enumerate(operations):
        if(val[0] not in initial_dict or val[2] not in initial_dict):
            skipped = True
            continue
        else:

            if(val[1] == 'AND'):
                initial_dict[val[3]] = (int(initial_dict[val[0]]) & int(initial_dict[val[2]]))
            elif(val[1] == 'OR'):
                initial_dict[val[3]] = (int(initial_dict[val[0]]) | int(initial_dict[val[2]]))
            elif(val[1] == 'XOR'):
                initial_dict[val[3]] = (int(initial_dict[val[0]]) ^ int(initial_dict[val[2]]))
            pass 

arr =[]
for key,value in initial_dict.items():
    if(key.startswith("z")):
        arr.append((key[1:],value))
(arr.sort())
(arr.reverse())
binary = ''
for j in arr:
    binary += str((j[1]))
print("Part 1 = ", int(binary,2))
