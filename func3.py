import networkx as nx
import init
import random

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts


# shortest path between the vertices
def shortest_path(graph, start, end):
    # if there is no edge between two vertices, random generate until the path is found
    while not nx.has_path(graph, start, end):
        i=0
        while (i<40):
            a = random.choice(init.vertex)
            b = random.choice(init.vertex)
            if graph.has_edge(a, b) and not graph.has_edge(b, a):
                continue
            if a != b:
                graph.add_edge(a, b, weight=init.weight_dicts[a + b])
            i += 1
    return nx.shortest_path(graph, start, end)
