# Mateusz Wróbel
from kol2testy import runtests
from math import inf
from queue import PriorityQueue

#Rozwiazanie O(Elog(V))

def lets_roll(start_city, flights, resorts):
    G = edges_to_graph(flights)
    _resorts = {}
    R = len(resorts)

    for r in resorts:
        # True - mozna uzyc
        # False - uzyty
        _resorts[r] = True
    cost = 0

    for i in range(R):
        cost += modified_dijkstra(G, start_city, _resorts)

    return cost * 2


def modified_dijkstra(G, s, _resort):
    n = len(G)
    d = [inf for _ in range(n)]
    d[s] = 0
    q = PriorityQueue()
    q.put((0, s))  # time,v,

    while not q.empty():
        time, v = q.get()

        if time > d[v]:
            continue
        # jesli jeszcze nie odwiedzilismy resortu
        if v in _resort and _resort[v]:
            _resort[v] = False
            return time

        for u, w in G[v]:
            #nie przechodzimy przez resort znowu
            if u in _resort and not _resort[u]:
                continue
            if d[u] > time + w:
                d[u] = time + w
                q.put((time + w, u))
    return d


def edges_to_graph(E):
    n = 0
    for u, v, w in E:
        n = max(u + 1, v + 1, n)
    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    return G


runtests(lets_roll, all_tests=True)
