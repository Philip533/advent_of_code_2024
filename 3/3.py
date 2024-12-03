import re
import os
# Routine to take in a slice of a character
# and perform the multiplication if it is of the valid
# form
def perform_multiply(mul_slice, do):

    product = 0
    test = (re.search("\\(\\d{1,3}\\,\\d{1,3}\\)", mul_slice))

    if (test):
        pair = (test.group(0))
        num1 = pair.split(",")[0][1:]
        num2 = pair.split(",")[1][:-1]
        if(do):
            product = int(num1) * int(num2)
    return product

# Change do and don't to YES and NO for easier parsing
os.system('sed "s/do[^n]/YES/g" input.in > input1.in')
os.system('sed "s/don/NO/g" input1.in > input_new.in')
os.system("rm input1.in")
f1 = open("input_new.in", "r")


counter = 0
# Part 1
# Loop over each line
for i in f1.readlines():

    # Go through each character
    for j, char in enumerate(i):

        # If we match "mu" then we know we have a multiply
        if(char == "m" and i[j+1] == "u"):
            counter += (perform_multiply(i[j:j+12], True))
print("Part 1 answer = ", counter)
        

f1.seek(0)
counter = 0
# Part 2
do = True
for i in f1.readlines():
    # print(i)
    for j, char in enumerate(i):
        # print(j, char)

        # Switch on multiplly
        if (char == "Y" and i[j+1] == "E"):
            do = True
        # Switch off multiply
        if (char == "N" and i[j+1] == "O"):
            do = False
        if(char == "m" and i[j+1] == "u"):
            counter += (perform_multiply(i[j:j+12], do))
print("Part 2 answer = ",counter)
os.system("rm input_new.in")
