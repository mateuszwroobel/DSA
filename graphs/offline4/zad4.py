from zad4testy import runtests

from queue import PriorityQueue
from math import inf

def spacetravel( n, E, S, a, b ):
    d = dijkstra(E,S,n,a)
    if d[b] != inf:
        return d[b]
    else:
        return None

def edges_to_graph(S,E,n):
    G = [[] for _ in range(n)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    return G

#osobliwosci
def add_edges_with_weight_0(S,G):
    for v in S:
        for u in S:
            G[v].append((u,0))
            G[u].append((v,0))

def dijkstra(E,S,n,s):
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((0,s))
    G = edges_to_graph(S,E,n)
    add_edges_with_weight_0(S,G)
    while not q.empty():
        dist, v = q.get()
        for u,w in G[v]:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                parent[u] = v
                q.put((d[u],u))
    return d
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
