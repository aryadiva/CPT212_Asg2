import networkx as nx
from matplotlib import pyplot as plt
import init

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

def mstt():
    T = nx.algorithms.minimum_spanning_tree(graph.to_undirected())
    print(T)
    nx.draw_networkx(T, with_labels=True, node_size=1500, node_color='grey', edge_color='grey', arrowsize=22,
                     font_size=16)
    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();
mstt()



