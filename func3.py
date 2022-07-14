import networkx as nx
import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

def spa(a, b):
    K=nx.algorithms.shortest_paths(graph, a, b)
    print(K);
