from math import inf
from queue import PriorityQueue


def abus(KR, OD, B, s, t):
    G = edge_to_adj(KR)
    d = modified_dijkstra(G, OD, B, s, t)
    if d != inf:
        return d
    else:
        return -1


def modified_dijkstra(G, OD, b, s, t):
    n = len(G)
    # d[v][k] =
    # d[v][k]- minimalna liczba butelek wody aby dotrzec do wierzcholka v majac "k" wody
    d = [[inf for _ in range(b + 1)] for _ in range(n)]
    q = PriorityQueue()
    d[s][b] = 1 #kupione wody (kupuje wode na sam poczatek)
    q.put((1,0,b ,s))  # liczba butelek ktoer juz kupilismy, time, woda pozostala, v
    while not q.empty():
        bought, time, water, v = q.get()
        if d[v][water] < bought:
            continue
        # pomijam pierwszy wierzcholek
        if v != s:
            # czekanie na nastepny autobus
            if time % OD[v] != 0:
                wait = OD[v] - (time % OD[v])
            else:
                wait = 0
            if water - wait < 0:
                # kupuje wode
                bought += 1
                # woda pozostala po kupnie i wypiciu
                water = b - (wait - water)
            else:
                # woda po oczekiwaniu
                water -= wait
            time += wait

        for u, w in G[v]:
            # sprawdzam czy moge dojechac bez wody
            if water - w >= 0:
                if d[u][water - w] > bought:
                    d[u][water - w] = bought
                    q.put((bought,time + w, water - w,u))
            # sprawdzam czy wgl waga przekracza b
            elif b - w >= 0:
                if d[u][b - w] > bought + 1:
                    d[u][b - w] = bought + 1
                    q.put((bought + 1,time + w, b-w, u))
            #wyjatek
            if d[u][0] > bought + 1:
                d[u][0] = bought + 1
                q.put((bought + 1, time + w, 0, u))
    return min(d[t])

def edge_to_adj(KR):
    # liczba wierzcholkow
    n = max(max(u, v) for u, v, w in KR) + 1
    # Tworze liste sasiedztwa
    G = [[] for _ in range(n)]
    for u, v, w in KR:
        G[u].append((v, w))
        G[v].append((u, w))
    return G

"""
Prosimy o niemodyfikowanie poniższego kodu :)
"""

line = input()
data = list(map(int, line.strip().split()))
E, V, b, s, t = data[:5]
KR = []
for i in range(5, 5 + E*3, 3):
    KR.append((data[i], data[i+1], data[i+2]))
OD = data[len(data) -  V: len(data)]
print(abus(KR, OD, b, s, t))

KR = [(0, 4, 4), (0, 1, 7), (1, 3, 6), (4, 3, 2), (1, 2, 1), (3, 2, 3)]
OD = [1, 6, 1, 8, 4]
B = 10;
s = 0;
t = 2
print(abus(KR, OD, B, s, t))
