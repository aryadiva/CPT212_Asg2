
adj_list={
    "Dushanbe":["Vaduz","Bamako","Podgorica","Sofia"],
    "Podgorica":["Sofia"],
    "Vaduz":["Bamako","Podgorica","Sofia"],
    "Bamako":["Podgorica","Sofia"],
    "Sofia":[]
    
}
print(adj_list)
color={}
parent={}

for u in adj_list.keys():
    color[u]='W'
    parent[u]=None
    
def dfs(u,color,parent):
    color [u]='G'
    for v in adj_list[u]:
        if color [v]=='W':
            cycle=dfs(v,color,parent)
            if cycle==True :
                return True
        elif color[v]=='G':
            print("Cycle Found",u,v)
            return True
    color[u]='B'
    return False
  
is_cyclic = False
for u in adj_list.keys():
    if color[u]=='W':
         if_cyclic=dfs(u,color,parent)
         if if_cyclic == True:
             break
print("Is Cyclic",is_cyclic)

