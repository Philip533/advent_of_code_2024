import numpy as np
import networkx as nx

f = open("input.in", "r")

gridsize = 71
count = 1
grid = np.zeros((gridsize,gridsize),dtype=str)

for i in f.readlines():

    # if(count > 1024):
        # break
    x, y = i.split(",")

    grid[int(y),int(x)] = '#'
    count += 1

    # print(grid)

    graph = nx.Graph()
    # Loop over grid and add nodes
    for i in range(gridsize):
        for j in range(gridsize):
            if(grid[i,j] == ''):
                graph.add_node((j,i))
    # print(graph.nodes())

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    for node in graph.nodes():

        for direction in directions:
            new_node = tuple(map(lambda i, j: i + j, node, direction))

            if (new_node in graph.nodes()):
                graph.add_edge(node, new_node)
                # print(e, new_node)

    print(x,y)
    print(nx.shortest_path_length(graph,(0,0),(gridsize-1, gridsize-1)))
        
