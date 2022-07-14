import init

vertex = init.vertex
edges = init.edges
dist = init.weight_dicts

## looping through a list of distance to find the correct distance
def dist_loop(j, k):
    temp1 = (j+k)
    for x in dist:
        if(temp1 == x):
            result = dist[x]
    return result

# Add edges function
def add(a, b):
    for x in vertex:
        if(x == a):
            a = x;
        if(x == b):
            b = x;
            dist = dist_loop(a, b)
            edges.append((a,b,dist))
            break;