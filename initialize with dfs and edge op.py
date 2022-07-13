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

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)

    def get_neighbors(self):
        return self.neighbors

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance


# Define directed graph

class DirectedGraph:
    def __init__(self):
        self.vertices = []
        self.add_vertex(Vertex("BA"))
        self.add_vertex(Vertex("VA"))
        self.add_vertex(Vertex("PO"))
        self.add_vertex(Vertex("SO"))
        self.add_vertex(Vertex("DU"))
        self.add_edge(self.get_vertex("BA"), self.get_vertex("VA"), 4196)
        self.add_edge(self.get_vertex("VA"), self.get_vertex("PO"), 929)
        self.add_edge(self.get_vertex("PO"), self.get_vertex("SO"), 334)
        self.add_edge(self.get_vertex("SO"), self.get_vertex("DU"), 3817)
        self.add_edge(self.get_vertex("DU"), self.get_vertex("BA"), 7991)

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

    # remove edge from graph
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            if vertex2 in self.vertices:
                vertex1.remove_neighbor(vertex2)
            else:
                print("Vertex not in graph")

    # print graph with weights
    def print_graph_with_weights(self):
        for vertex in self.vertices:
            print(vertex.name)
            for neighbor in vertex.neighbors:
                print("\t" + neighbor.name + " " + str(vertex.get_distance()))
            print("\n")

    # dfs
    def dfs(self, vertex, visited):
        visited.append(vertex)
        for neighbor in vertex.neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # check if graph is strongly connected
    def is_strongly_connected(self):
        visited = []
        for vertex in self.vertices:
            if vertex not in visited:
                self.dfs(vertex, visited)
        if len(visited) == len(self.vertices):
            return True
        else:
            return False


if __name__ == "__main__":
    # create directed graph
    graph = DirectedGraph()

    # print graph with weights
    graph.print_graph_with_weights()

    # check if graph is strongly connected
    if graph.is_strongly_connected():
        print("Graph is strongly connected")
    else:
        print("Graph is not strongly connected")
