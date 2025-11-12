from zad3testy import runtests
from collections import deque

def longer( G, s, t ):
    dt,edges = BFS(G,s,t)
    min1 = min(dt)
    index = None
    for i in range(len(dt)):
        if dt[i] == min1:
            index = i
            break
    bridge = find_bridge(G)
    #print(G)
    if len(bridge) == 0 or (s <= bridge[0][0] and t <= bridge[0][0]) or (t >= bridge [0][1] and s >= bridge[0][1]) :
        return edges[index]
    else:
        print("most",bridge)

        return bridge[0]

def BFS(G,s,t):
    n = len(G)
    inf = float('inf')
    d = [inf for _ in range(n)]
    visited = [False for _ in range (n)]
    d[s] = 0
    d_t = []
    visited[s] = True
    q = deque()
    q.append(s)
    k = 0
    edges = []
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                q.append(v)
            if v == t:
                d_t.append(d[u] + 1)
                edges.append((u,t))
    return d_t,edges

def find_bridge(G):
    n = len(G)
    inf = float('inf')
    time = 0
    visited = [False for _ in range(n)]
    low = [inf for _ in range(n)]
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    bridges = []

    def dfs_visit(G,v):
        nonlocal time,d
        time+=1
        visited[v] = True
        d[v] = time
        low[v] = time
        for u in G[v]:     #v-parent, u-child
            if not visited[u]:
                parent[u] = v
                dfs_visit(G,u)
                low[v] = min(low[v],low[u])
            elif visited[u] and (u!=parent[v]): #back edge
                low[v] = min(low[v],d[u])
        if low[v] == d[v] and parent[v] is not None:
            bridges.append((parent[v],v))

    for v in range(n):
        if not visited[v]:
            dfs_visit(G,v)
    #print(d)
    return bridges

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
