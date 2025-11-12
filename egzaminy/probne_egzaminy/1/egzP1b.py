from egzP1btesty import runtests
from queue import PriorityQueue
from math import inf


def turysta(G, D, L):
    g = edge_to_adj(G)
    d = modified_dijkstra(g,D,L)
    return d


def modified_dijkstra(G, s,t):
    n = len(G)
    # d[v][k] = najkrotsza odl do wierzcholka "v" od "s", "k" ktory to wiezrcholek od zrodla
    d = [[inf] * 5 for _ in range(n)]
    q = PriorityQueue()
    d[s][0] = 0
    q.put((0, s, 0)) # dist, v, number vertex in path
    while not q.empty():
        dist, v, k = q.get()
        if dist > d[v][k]:
            continue

        if v == t and k == 4:
            return dist

        for u, w in G[v]:
            if k < 4:
                if d[u][k + 1] > dist + w:
                    d[u][k + 1] = dist + w
                    q.put((dist + w, u, k + 1))
    return d[t][4]

def edge_to_adj(E):
    n = 0
    for u, v, w in E:
        n = max(n, u + 1, v + 1)
    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    return G

runtests(turysta)
