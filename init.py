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
DU_VA = 4805;   PO_SO = 334;    VA_BA = 4168;   VA_PO = 929;    DU_PO = 4149;
BA_PO = 4226;   VA_SO = 1192;   BA_SO = 4495;   DU_BA = 7991;   DU_SO = 3817;

dist = [["DU_VA", DU_VA], ["PO_SO", PO_SO], ["VA_BA", VA_BA], ["VA_PO", VA_PO], ["DU_PO", DU_PO],
        ["BA_PO", BA_PO], ["VA_SO", VA_SO], ["BA_SO", BA_SO], ["DU_BA", DU_BA], ["DU_SO", DU_SO]]

# Initialize vertex using adjacency list
vertex = ['BA', 'VA', 'PO', 'SO', 'DU']
# Initialize edges
edges = [('BA', 'VA', VA_BA), ('VA', 'PO', VA_PO), ('PO','SO', PO_SO), ('SO', 'VA', VA_SO), ('DU', 'BA', DU_BA)]
# Initialize position
pos = { 'BA': [1,2] , 'VA': [3,2] , 'PO': [3,1], 'SO': [2,1.25], 'DU': [1,1]}

graph = nx.DiGraph()
def draw_graph():
    graph.add_nodes_from(vertex)
    graph.add_weighted_edges_from(edges)
    weight = nx.get_edge_attributes(graph, 'weight')

    nx.draw(graph, pos=pos, with_labels=True, node_size=1000, arrowsize=25)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weight)

    ax = plt.gca()
    ax.margins(0.005)
    plt.axis("off")
    plt.show();
