import numpy as np
from functools import cache

import matplotlib.pyplot as plt
import networkx as nx
import re
from itertools import product

f = open("input.in", "r")

def match(position):
    global patterns
    global line
    for pattern in patterns:
        if(line[position:position+len(pattern)] == pattern):
            new_position = position + len(pattern)
            if(new_position == len(line)):
                return True
            if(match(new_position)):
                return True
    return False



rules = (f.readline().strip().split(","))
patterns = []
for i in rules:
    patterns.append(i.lstrip())

counter = 0
timer = 0
for i in f.readlines():
    timer += 1
    if(not i.split()):
        continue
    
    line = i.strip()

    if(match(0)):
        counter += 1
print(counter)
