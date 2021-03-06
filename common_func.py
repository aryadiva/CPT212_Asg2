from matplotlib import pyplot as plt
import networkx as nx
import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts


## looping through a list of distance to find the correct distance
def dist_loop(j, k):
    temp1 = (j + k)
    for x in dist:
        if (temp1 == x):
            result = dist[x]
    return result


# Add function
def add(a, b):
    if ((graph.has_edge(a, b) == True)):
        print('The edge ( %s , %s ) already exists!' % (a, b))
    else:
        edge = [(a, b, dist[a + b])]
        graph.add_weighted_edges_from(edge)
        print('The edge ( %s , %s ) is added!' % (a, b))
    init.draw_graph()


# add edge validation function
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
    add(n, m)


def remove(a, b):
    if (graph.has_edge(a, b) == True):
        graph.remove_edge(a, b)
        print('The edge has been removed')
    else:
        print('The edge to be removed is non-existant')
    init.draw_graph()


# Remove edges validation function
def remove_edges():
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
    remove(n, m)

def FetchStart():
    while True:
        a = input("Please input the starting vertex: ")
        i = 0
        while i <= len(vertex):
            temp = vertex[i]
            if (temp == a):
                break
            i += 1
            if (i == 5 and temp != a):
                print("Unknown input, terminating...")
                quit()
        break
    return fetch(a)

def FetchEnd():
    while True:
        b = input("Please input the destination vertex: ")
        i = 0
        while i <= len(vertex):
            temp = vertex[i]
            if (temp == b):
                break
            i += 1
            if (i == 5 and temp != b):
                print("Unknown input, terminating...")
                quit()
        i = 0
        break
    return fetch(b)

def fetch(a):
    if(a == 'BA'):
        return 0
    elif(a == 'VA'):
        return 1
    elif(a == 'PO'):
        return 2
    elif(a == 'SO'):
        return 3
    elif(a == 'DU'):
        return 4

# reset the graph
def reset():
    graph.clear()
    graph.add_nodes_from(vertex)
    graph.add_weighted_edges_from(edges)
    weight = nx.get_edge_attributes(graph, 'weight')
    print('The graph has been reset')
