def dfs_time(G):
    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    d = [-1 for i in range(n)]
    def dfs_visit(G,v):
        nonlocal time
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfs_visit(G,u)
        time+=1
        d[v] = time
    for v in range(n):
        if not visited[v]:
            dfs_visit(G,v)
    return d

def descent_order(G,d):
    n = len(G)
    order = sorted(range(n), key=lambda i: d[i], reverse=True)
    return order

def reverse_edges(G):
    n = len(G)
    g1 = [[] for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            g1[v].append(i)
    return g1

def coherent_components(G):
    n = len(G)
    d = dfs_time(G)
    g1 = reverse_edges(G)
    order = descent_order(G,d)
    visited = [False for i in range(n)]
    components = []

    def dfs(G,v,component):
        visited[v] = True
        component.append(v)

        for u in G[v]:
            if not visited[u]:
                dfs(G,u,component)

    for i in order:
        if not visited[i]:
            component = []
            dfs(g1,i,component)
            components.append(component)
    return components

g = [[3, 1],
 [2, 10],
 [3],
 [4],
 [2, 5],
 [2],
 [5, 9],
 [6],
 [7],
 [8],
 [9, 0]]

print(coherent_components(g))
