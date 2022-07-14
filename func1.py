import init
import networkx as nx


# check if the graph is strongly connected
def is_strongly_connected(graph):
    return nx.is_strongly_connected(graph)

# generate random edges between random vertex until the graph is strongly connected
def generate_strongly_connected_graph(graph):
    while not is_strongly_connected(graph):
        a = random.choice(init.vertex)
        b = random.choice(init.vertex)
        if (a != b):
            graph.add_edge(a, b)
    return graph