import func1
import func3
import func4
import init
from common_func import add
from common_func import add_edge
from common_func import remove_edges
from func1 import is_strongly_connected

graph = init.graph
vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## This file is for the main menu or main UI
def main_menu():
    init.draw_graph()
    print('-----------------------------------\n'
        '|            Main Menu            |\n'
        '-----------------------------------\n'
        '|  1. Add Edge                    |\n'
        '|  2. Remove Edge                 |\n'
        '|  3. Check Connectivity Graph    |\n'
        '|  4. Check Cyclic Graph          |\n'
        '|  5. Calculate Shortest Path     |\n'
        '|  6. Show Minimum Spanning Tree  |\n'
        '|  7. Reset                       |\n'
        '|  8. Exit                        |\n'
        '-----------------------------------\n')

def options():
    while True:
        c = input("Choose: ")
        if (c == '1'):
            add_edge()
        if (c == '2'):
            remove_edges()
        if (c == '3'):
            print(func1.is_strongly_connected(graph))
            print(func1.generate_strongly_connected_graph(graph))
            # func1
        if (c == '4'):
            None
            # func2
        if (c == '5'):
            None
            # func3
        if (c == '6'):
            func4.mstt()
        if (c == '7'):
            None
            # reset
        if (c == '8'):
            quit()

# user inputting new edges -----------
def min_ST():
    while True:
        while True:
            n = input("Please input the starting vertex: ")
            i = 0
            while i <= len(vertex):
                temp = vertex[i]
                if (temp == n):
                    break
                i += 1
                if (i == 5 and temp != n):
                    print("Unknown input, terminating...")
                    quit()
            break

        while True:
            m = input("Please input the destination vertex: ")
            i = 0
            while i <= len(vertex):
                temp = vertex[i]
                if (temp == m):
                    break
                i += 1
                if (i == 5 and temp != m):
                    print("Unknown input, terminating...")
                    quit()
            i = 0
            break

        add(n, m);
        init.draw_graph()
        func4.mstt()
        print("Add more? y/n")
        q = input()
        if (q == "n"):
            quit()
        if (q == "y"):
            continue
        if (q != "n" and q != "y"):
            print("Not a valid response, exiting...")
            quit()
#---------------------------------------
main_menu()
options()
#options(c)

