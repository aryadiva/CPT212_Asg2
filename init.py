# Optimize imports
import networkx as nx
import matplotlib.pyplot as plt

"""
BA = Bamako, VA = Vaduz, PO = Podgorica, SO = Sofia , DU = Dushanbe

DU --> BA --> VA --> PO --> SO --> VA

# Distance list (Km)
DU <--> VA = 4805   PO <--> SO = 334    VA <--> BA = 4168   VA <--> PO = 929    DU <--> PO = 4149
BA <--> PO = 4226   VA <--> SO = 1192   BA <--> SO = 4495   DU <--> BA = 7991   DU <--> SO = 3817
"""
# Initialize distance
DU_VA = 4805;
PO_SO = 334;
VA_BA = 4168;
VA_PO = 929;
DU_PO = 4149;
BA_PO = 4226;
VA_SO = 1192;
BA_SO = 4495;
DU_BA = 7991;
DU_SO = 3817;

weight_dicts = {
    'DUVA': 4805,
    'DUBA': 7991,
    'DUPO': 4149,
    'DUSO': 3817,
    'POSO': 334,
    'PODU': 4149,
    'POBA': 4226,
    'POVA': 929,
    'VADU': 4805,
    'VABA': 4168,
    'VAPO': 929,
    'VASO': 1192,
    'BADU': 7991,
    'BAPO': 4226,
    'BASO': 4495,
    'BAVA': 4168,
    'SODU': 3817,
    'SOPO': 334,
    'SOVA': 1192,
    'SOBA': 4495
}

# Initialize vertex using adjacency list
vertex = ['BA', 'VA', 'PO', 'SO', 'DU']
# Initialize edges
edges = [('BA', 'VA', VA_BA), ('VA', 'PO', VA_PO), ('PO', 'SO', PO_SO), ('SO', 'VA', VA_SO), ('DU', 'BA', DU_BA)]
# Initialize position
pos = {'BA': [1, 2], 'VA': [3, 2], 'PO': [3, 1], 'SO': [2, 1.25], 'DU': [1, 1]}

graph = nx.DiGraph()

def draw_graph_init():
    graph.add_nodes_from(vertex)
    graph.add_weighted_edges_from(edges)
    weight = nx.get_edge_attributes(graph, 'weight')

    nx.draw(graph, pos=pos, with_labels=True, node_size=1000, arrowsize=22)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weight)

    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();

def draw_graph():
    Weight = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx(graph, with_labels=True, pos= pos, node_size =1000, arrowsize = 22)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels = Weight)

    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();


