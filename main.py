import func4
import init
from common_func import add
from func1 import is_strongly_connected

vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## This file is for the main menu or main UI
def main_menu():
    print('-----------------------------------\n'
        '|            Main Menu            |\n'
        '-----------------------------------\n'
        '|  1. Show Graph                  |\n'
        '|  2. Add Edge                    |\n'
        '|  3. Remove Edge                 |\n'
        '|  4. Check Connectivity Graph    |\n'
        '|  5. Check Cyclic Graph          |\n'
        '|  6. Calculate Shortest Path     |\n'
        '|  7. Show Minimum Spanning Tree  |\n'
        '|  8. Reset                       |\n'
        '|  9. Exit                        |\n'
        '-----------------------------------\n')

def options(c):
    while True:
        if (c == 1):
            # show graph
        elif (c == 2):
            # add edge
        elif (c == 3):
            # remove edge
        elif (c == 4):
            # func1
        elif (c == 5):
            # func2
        elif (c == 6):
            # func3
        elif (c == 7):
            # func4
        elif (c == 8):
            # reset
        elif (c == 9):
            # exit
            break


# user inputting new edges -----------
def min_ST():
    while True:
        init.draw_graph()
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
            ...
min_ST()
#---------------------------------------
