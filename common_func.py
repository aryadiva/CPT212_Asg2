from matplotlib import pyplot as plt

import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## looping through a list of distance to find the correct distance
def dist_loop(j, k):
    temp1 = (j+k)
    for x in dist:
        if(temp1 == x):
            result = dist[x]
    return result

# Add function
def add(a, b):
    if ((graph.has_edge(a, b) == True) or (graph.has_edge(b, a))):
        print('The edge ( %s , %s ) already exists!' % (a, b))
    else:
        edge = [(a, b, dist[a+b])]
        graph.add_weighted_edges_from(edge)
        print('The edge ( %s , %s ) is added!' % (a, b))
    init.draw_graph()
# add edge function
def add_edge():
    while True:
        n = input("Please input the starting vertex: ")
        i = 0
        while i <= len(vertex):
            temp = vertex[i]
            if (temp == n):
                break
            i += 1
            if (i == 5 and temp != n):
                print("Unknown input, terminating...")
                quit()
        break

    while True:
        m = input("Please input the destination vertex: ")
        i = 0
        while i <= len(vertex):
            temp = vertex[i]
            if (temp == m):
                break
            i += 1
            if (i == 5 and temp != m):
                print("Unknown input, terminating...")
                quit()
        i = 0
        break
    add(n,m)

# Remove edges function
def remove_edges() :
    del edges[0]
    print(edges)
    graph.clear()
    init.draw_graph()
