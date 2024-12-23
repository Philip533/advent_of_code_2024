import networkx as nx

f = open("input.in", "r")
graph = nx.Graph()

for i in f.readlines():
    x,y = (i.strip().split("-"))
    # print(x,y)
    graph.add_node(x)
    graph.add_node(y)
    graph.add_edge(x,y)

counter = 0
for x in (nx.enumerate_all_cliques(graph)):
    # print(x)
    if(len(x) == 3):
        for j in x:
            if(j[0] == 't'):
                counter += 1
                break
print("Part 1 = ", counter)
connected = []
for x in (nx.enumerate_all_cliques(graph)):
    connected = x
connected.sort()
print("Part 2 = ",','.join(connected))

