from kol3btesty import runtests
from math import inf
from queue import PriorityQueue
#dodaje wierzcholek "x" i tworze polaczenie
# u-x-v o wagach odpowiednio: w(u,x) = A[u], w(x,v) = A[v]
def airports(G, A, s, t):
    n = len(G)
    G.append([])
    for i in range(n):
        G[n].append((i,A[i]))
        G[i].append((n,A[i]))
    return dijkstra(G,s,t)

def dijkstra(G,s,t):
    n= len(G)
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((0, s))
    while not q.empty():
        dist, v = q.get()
        if v == t:
            return dist
        if dist > d[v]:
            continue
        for u, w in G[v]:
            if d[u] > dist + w:
                d[u] = dist + w
                q.put((d[u], u))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
