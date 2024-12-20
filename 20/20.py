import numpy as np
import tqdm 
import networkx as nx

f = open("input.in")

matrix = [list(i.strip()) for i in f.readlines()]
matrix = np.array(matrix)
print(matrix)

hash_list = []
save_dict = {}
graph = nx.grid_2d_graph(len(matrix), len(matrix))
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if(matrix[i,j] == '#'):
            graph.remove_node((i,j))
            hash_list.append((i,j))

        if(matrix[i,j] == 'S'):
            start = (i,j)
        if(matrix[i,j] == 'E'):
            end = (i,j)

initial_length = nx.dijkstra_path_length(graph,start,end)

# print(hash_list)
for i in tqdm.tqdm(hash_list:
    j,k = i
    graph.add_node(i)
    graph.add_edge(i,(j+1,k))
    graph.add_edge(i,(j-1,k))
    graph.add_edge(i,(j,k+1))
    graph.add_edge(i,(j,k-1))
    if((nx.dijkstra_path_length(graph, start,end)) in save_dict):
        save_dict[(nx.dijkstra_path_length(graph, start,end))] += 1
    else:
        save_dict[(nx.dijkstra_path_length(graph, start,end))] = 1
    graph.remove_node(i)
print(save_dict)

counter = 0
for vals in save_dict.keys():
    if(initial_length - vals >= 100):
        counter += (save_dict[vals])
print("Part 1 answer = ", counter)

