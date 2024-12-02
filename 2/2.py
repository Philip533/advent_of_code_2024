import numpy as np
f = open("input.in", "r")

# Checks if a line is safe
def check_line_safe(line):

    diff = np.array(np.diff(line))
    sign = np.array(np.sign(diff))
    
    if(np.all(sign == 1)):
        if(np.all(abs(diff) <= 3)):
            return True
    if(np.all(sign == -1)):
        if(np.all(abs(diff) <= 3)):
            return True
    return False

counter1 = 0
counter2 = 0

## Part 1
# Get each line
for i in f.readlines():
    line = i.split()
    line = np.array(line,dtype="int")
    if(check_line_safe(line)):
        counter1 += 1
        continue

## Part 2
    # Brute force solution! Just delete 1 value in each unsafe line :)
    # and if safe, skip to next line
    for j in range(len(line)):
        new_line = np.delete(line, j)
        if(check_line_safe(new_line)):
            counter2 += 1
            break

print("Part 1 solution = ",counter1)
print("Part 2 solution = ",counter1+counter2)


