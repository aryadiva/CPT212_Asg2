import networkx as nx

import common_func
import init
import random

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts


# shortest path between the vertices
def shortest_path(graph, start, end):
    # if there is no edge between two vertices, random generate until the path is found
    if not nx.has_path(graph, start, end):
        while (nx.has_path(graph, start, end)==False):
            a = random.choice(init.vertex)
            b = random.choice(init.vertex)
            if graph.has_edge(a, b) and not graph.has_edge(b, a):
                continue
            if a != b:
                graph.add_edge(a, b, weight=init.weight_dicts[a + b])
        init.draw_graph()
        return nx.shortest_path(graph, start, end)
    else:
        return nx.shortest_path(graph, start, end)