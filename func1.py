import init
import networkx as nx
import random


# check if the graph is strongly connected
def is_strongly_connected(graph):
    return nx.is_strongly_connected(graph)


# generate random edges between random vertex until the graph is strongly connected
def generate_strongly_connected_graph(graph):
    # remove all edges
    while not is_strongly_connected(graph):
        a = random.choice(init.vertex)
        b = random.choice(init.vertex)
        # if already have an edge between two vertices, then skip
        if graph.has_edge(a, b) and not graph.has_edge(b, a):
            continue
        if a != b:
            graph.add_edge(a, b, weight=init.weight_dicts[a + b])
    init.draw_graph()
    return graph
