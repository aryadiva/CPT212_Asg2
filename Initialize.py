# Define vertex
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = 0
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance


# define directed graph

class DirectedGraph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def get_vertex(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        return None

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices:
            if vertex2 in self.vertices:
                vertex1.add_neighbor(vertex2)
                vertex1.set_distance(weight)
            else:
                print("Vertex not in graph")
        else:
            print("Vertex not in graph")

# print graph with weights

    def print_graph_with_weights(self):
        for vertex in self.vertices:
            print(vertex.name)
            for neighbor in vertex.neighbors:
                print("\t" + neighbor.name + " " + str(vertex.get_distance()))
            print("\n")

# check if graph is strongly connected

    def is_strongly_connected(self):
        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True


if __name__ == "__main__":
    # create directed graph
    graph = DirectedGraph()
    # add vertices
    graph.add_vertex(Vertex("BA"))
    graph.add_vertex(Vertex("VA"))
    graph.add_vertex(Vertex("PO"))
    graph.add_vertex(Vertex("SO"))
    graph.add_vertex(Vertex("DU"))

    # add edges
    graph.add_edge(graph.get_vertex("BA"), graph.get_vertex("VA"), 4196)
    graph.add_edge(graph.get_vertex("VA"), graph.get_vertex("PO"), 929)
    graph.add_edge(graph.get_vertex("PO"), graph.get_vertex("SO"), 334)
    graph.add_edge(graph.get_vertex("SO"), graph.get_vertex("DU"), 3817)
    graph.add_edge(graph.get_vertex("DU"), graph.get_vertex("BA"), 7991)

    # print graph with weights
    graph.print_graph_with_weights()

    # check if graph is strongly connected
    print(graph.is_strongly_connected())