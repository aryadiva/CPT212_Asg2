import networkx as nx
import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

def spa():
    init.draw_graph_init()
    print("Please input the starting vertex: ")
    n = input()
    print("Please input the destination vertex: ")
    m = input()

    K=nx.algorithms.shortest_paths(graph, n, m)
    print(K);