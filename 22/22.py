import numpy as np

f = open("input.in")

length = 2000
lines = len(f.readlines())
matrix = np.zeros((lines, length-1))
matrix2 = np.zeros((lines, length))
f.seek(0)
counter = 0
index_count = 0
for i in f.readlines():

    init_num = int(i)
    arr = np.zeros(length)
    diff_arr = np.zeros(length-1)
    for j in range(length):

        arr[j] = int((str(init_num)[-1]))
        new_num = init_num * 64

        new_num2 = new_num ^ init_num

        prune = new_num2 % 16777216

        div = int(prune/32) ^ prune

        prune2 = div % 16777216

        new_num3 = prune2 * 2048

        mix3 = new_num3 ^ prune2


        new_num3 = mix3 % 16777216
        init_num = new_num3
    counter += new_num3
    # print(arr)
    diff_arr = np.diff(arr)
    matrix[index_count, :] = diff_arr
    matrix2[index_count, :] = arr
    index_count += 1

print("Part 1 = ", counter)

dictlist = [dict() for x in range(lines)]

mat_count = 0
for j in matrix:

    seen = set()
    for k in range(0,len(j)-3,1):

        sequence = (int(j[k]),int(j[k+1]),int(j[k+2]), int(j[k+3]))

        if(sequence not in seen):
    
            dictlist[mat_count][sequence] = int(matrix2[mat_count,k+4])
            seen.add(sequence)

    mat_count += 1
new_dict = {}

for i in dictlist:

    for j,k in i.items():
        new_dict[j] = 0

# print(new_dict)
for m,i in enumerate(dictlist):

    # print(i)
    for j,k in i.items():
        # print(j,k)
        new_dict[j] += k
key = (max(new_dict, key=new_dict.get))
print("Part 2 answer = ", max(new_dict.values()))
