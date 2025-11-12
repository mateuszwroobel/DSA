from queue import PriorityQueue

from math import inf

n = 7
E = [(1, 5, 10), (4, 6, 12), (3, 2, 8), (2, 4, 4), (2, 0, 10), (1, 4, 5), (1, 0, 6), (5, 6, 8), (6, 3, 9)]
def edges_to_graph(E,n):
    G = [[] for _ in range(n)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    return G

def show_path(parent,t):
    path = []
    while t is not None:
        path.append(t)
        t = parent[t]
    return path


def dijkstra(E,n,s):
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((0,s))
    G = edges_to_graph(E,n)
    print(G)
    while not q.empty():
        dist, v = q.get()
        if dist > d[v]:
            continue
        for u,w in G[v]:
            if d[u] > dist + w:
                d[u] = dist + w
                parent[u] = v
                q.put((d[u],u))
    return d,parent

d,p = dijkstra(E,n,0)
print(d)



