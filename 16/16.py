import numpy as np
import tqdm
import networkx as nx

f = open("input.in", "r")

matrix = []
for i in f.readlines():
    line = [x for x in list(i)]
    matrix.append(line[:-1])
matrix = np.array(matrix)
print(matrix)


directions = [(-1,0), (0,1), (1,0), (0,-1)]
graph = nx.DiGraph()
for i in range(len(matrix)):
    for j in range(len(matrix)):

        if(matrix[i,j] == '.'):
            for direction in directions:
                graph.add_node(((i,j),direction))
        if(matrix[i,j] == 'S'):
            for direction in directions:
                graph.add_node(((i,j),direction))
        if(matrix[i,j] == 'E'):
            for direction in directions:
                graph.add_node(((i,j),direction))

def tuple_rotate(tup,direc):

    if(direc == 1):
        if(tup == (1,0)):
            return (0,-1)
        if(tup == (0,-1)):
            return (-1,0)
        if(tup == (-1,0)):
            return (0,1)
        if(tup == (0,1)):
            return (1,0)
    if(direc == -1):
        if(tup == (1,0)):
            return (0,1)
        if(tup == (0,1)):
            return (-1,0)
        if(tup == (-1,0)):
            return (0,-1)
        if(tup == (0,-1)):
            return (1,0)

for k, dk in graph.nodes:

    print(k+dk)
    add = tuple(map(lambda i, j: i + j, k, dk))
    # If same direction at next node, then weight is 1
    if (add, dk) in graph.nodes:
        graph.add_edge((k,dk), (add,dk), weight = 1)
    graph.add_edge((k,dk), (k,tuple_rotate(dk,-1)), weight = 1000)
    graph.add_edge((k,dk), (k,tuple_rotate(dk,1)), weight = 1000)
paths = nx.all_shortest_paths(graph, ((139,1),(0,1)), ((1,139),(-1,0)), weight="weight")
length = nx.shortest_path_length(graph, ((139,1),(0,1)), ((1,139),(-1,0)), weight="weight")
spot_list = []
for path in paths:

    for j,dj in path:
        print(j,dj)
        spot_list.append(j)

print(len(set(spot_list)))
print(length)
