import numpy as np
import networkx as nx
f = np.loadtxt("input.in", dtype=str)

matrix = np.array([list(x) for x in f])

# Possible directions which are tuples 
# so hashable for the graph
directions = [(0,-1), (1,0), (0,1), (-1,0)]

board = {}

# Loop over the grid
for index, val in enumerate(f):
    for index2, val2 in enumerate(val):

        # The dictionary key is a tuple of the indices,
        # and the value is the point on the grid
        board[(index,index2)] = val2

# Make an empty graph
G = nx.Graph()

# Loop over every point 
for z in board:

    # Loop over directions
    for direction in directions:

        # Weird tuple addition
        next_z = tuple(map(lambda i, j: i + j, z, direction))

        # Check if going off grid or not
        try:

            # If connected, we add the node and
            # make an edge connecting it
            if(board[z] == board[next_z]):
                G.add_node((next_z))
                G.add_edge(z, next_z)
        # If doesn't exist then just move on
        except KeyError:
            continue

# Add the single values that have no edges
G.add_nodes_from(board)

total = 0

edge_graph = nx.Graph()
part2_total = 0
# Loop over the groups of connected edges
for j in nx.connected_components(G):

    side_total = 0
    edge_graph = nx.Graph()
    wall_count = 0
    side_count = 0
    test_arr = []
    # Loop over each node
    for k in j:

        # Loop over directions again
        for direction in directions:

            next_z = tuple(map(lambda i, j: i + j, k, direction))

            if (next_z not in j):
                # print(k,next_z)

                if(direction == (-1, 0)):
                    next_z =(list(next_z))
                    next_z.append(0)
                    next_z = tuple(next_z)
                    edge_graph.add_node(next_z)
                if(direction == (0, 1)):
                    next_z =(list(next_z))
                    next_z.append(1)
                    next_z = tuple(next_z)
                    edge_graph.add_node(next_z)
                if(direction == (1, 0)):
                    next_z =(list(next_z))
                    next_z.append(2)
                    next_z = tuple(next_z)
                    edge_graph.add_node(next_z)
                if(direction == (0, -1)):
                    next_z =(list(next_z))
                    next_z.append(3)
                    next_z = tuple(next_z)
                    edge_graph.add_node(next_z)

                wall_count += 1
            # We want to see if we DON'T have a connection, because a wall will be there

    # print(edge_graph.nodes())

    for m in 0,1,2,3:

        side_count = 0
        direction_graph = nx.Graph()
        for k in edge_graph.nodes():

            y = k[0:2]

            if(k[2] == m):

                # Contains all the nodes which have a certain direction
                direction_graph.add_node(y)

        # print(direction_graph.nodes(), "DIR")

        # Loop over directions again to decide whether the nodes are connected
        for f in direction_graph.nodes():

            # print(f)
            for direction in directions:
                next_z = tuple(map(lambda i, j: i + j, f, direction))

                if(next_z in direction_graph.nodes()):
                    # print("HELLO", f, next_z)
                    # side_count += 1
                    direction_graph.add_edge(f,next_z)


        print(direction_graph.nodes())
        for k in nx.connected_components(direction_graph):
            side_count += 1
            # print(k)
        side_total += side_count

    area = len(j)
    print(area, side_total, area*side_total)
    part2_total += area*side_total
    cost = (area*wall_count)
    total += cost
    # print(test_arr)

# print(total)
print(part2_total)


