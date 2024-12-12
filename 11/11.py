import numpy as np

f = np.loadtxt("input.in", dtype=int)

count = 0

while count < 75:

    temp_arr = []

    if(count == 0):
        array = f
    for index, val in enumerate(array):

        if(val == 0):
            temp_arr.append(1)
        elif(len(str(val)) % 2 == 0):

            num = str(val)

            half = int(len(num)/2)
            num1 = num[0:half]
            num2 = num[half:]

            temp_arr.append(int(num1))
            temp_arr.append(int(num2))
            # print(num1, num2)
        else:
            temp_arr.append(int(val)*2024)


    array = temp_arr


    count += 1
    print(count)
print(len(temp_arr))
