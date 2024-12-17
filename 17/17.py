import numpy as np

f = open("input.in", "r")
registers = []
for i in f.readlines():
    registers.append(i.split(":")[1].strip())

instruction_str = list(registers.pop(3).split(","))

instructions = [int(x) for x in instruction_str]
registers = [int(x) for x in registers]
print(instructions)
print(registers)

def combo_op(op, registers):
    if(0 <= op <= 3):
        return op
    elif(op == 4):
        return registers[0]
    elif(op == 5):
        return registers[1]
    elif(op == 6):
        return registers[2]


# for index in range(0,len(instructions) - 2,2):
for i in range(0,1):
    registers[0] = i
    index = 0
    out_list = []
    while True:
        instruction = instructions[index]
        # Adv
        if(instruction == 0):

            power = combo_op(instructions[index+1], registers)
            numerator = registers[0]
            registers[0] = int(numerator/(2**power))
            index += 2

        # bxl
        elif(instruction == 1):

            registers[1] = (registers[1] ^ instructions[index+1])
            index += 2

        # bst
        elif(instruction == 2):

            val = combo_op(instructions[index+1], registers)
            registers[1] = val % 8
            index += 2

        # jnz
        elif(instruction == 3):

            if(registers[0] == 0):
                index += 2
            else:
                pass
                index = instructions[index+1]

        # bxc
        elif(instruction == 4):
            registers[1] = (registers[1] ^ registers[2])
            index += 2
        
        # out
        elif(instruction == 5):
            val = combo_op(instructions[index+1], registers)
            index += 2
            out_list.append(str(val%8))

        # bdv
        elif(instruction == 6):

            power = combo_op(instructions[index+1], registers)
            numerator = registers[0]
            registers[1] = int(numerator/(2**power))
            index += 2
        elif(instruction == 7):

            power = combo_op(instructions[index+1], registers)
            numerator = registers[0]
            registers[2] = int(numerator/(2**power))
            index += 2

        # print(registers)
        if(index >= len(instructions)-1):
            break
