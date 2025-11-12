from egz1atesty import runtests
from math import inf
from queue import PriorityQueue


def armstrong(B, G, s, t):
    #liczba wierzcholkow
    n = max(max(u,v) for u,v,w  in G) + 1
    b = best_bike(B, n)
    g = create_graphs(G,b,n)
    from_start = dijkstra(g, s)
    from_end = dijkstra(g,t)
    #szukam najlepszej sciezki
    #symulacja sciezki z s do t, zakldajac ze wsiadam w v na rower
    best = inf
    for v in range(n):
        #wsiadam na rower w "v"
        to_end = from_end[v] * b[v]
        path = from_start[v] + to_end
        best = min(best,path)
    return int(best)

def dijkstra(G, s):
    n = len(G)
    d = [inf] * n
    d[s] = 0
    q = PriorityQueue()
    q.put((0, s))
    while not q.empty():
        dist, v = q.get()
        if dist > d[v]:
            continue
        for u, w in G[v]:
            new_dist = dist + w
            if new_dist < d[u]:
                d[u] = new_dist
                q.put((new_dist, u))
    return d

def best_bike(B, n):
    b = [1 for _ in range(n)]
    for i, p, q in B:
        # wybieram najlepszy rower
        # 1 - pieszo
        b[i] = min(b[i], p / q)
    return b


def create_graphs(E,b,n):
    g = [[] for _ in range(n)]
    for u, v, w in E:
        g[u].append((v, w))
        g[v].append((u, w))
    return g


runtests(armstrong, all_tests=True)
