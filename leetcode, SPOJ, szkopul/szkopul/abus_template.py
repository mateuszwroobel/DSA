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
    # d[v][k]- minimalna liczba butelek wody aby dotrzec do wierzcholka v majac "k" wody
    d = [[inf for _ in range(b + 1)] for _ in range(n)]
    q = PriorityQueue()
    d[s][b] = 1 #kupione wody (kupuje wode na sam poczatek)
    q.put((1,0, b,s))  # liczba butelek ktoer juz kupilismy, woda pozostala, time, s
    while not q.empty():
        bought, time, water, v = q.get()
        if d[v][water] < bought:
            continue
        #nowe zmienne aby nie modyfikowac orygianlnych
        time_after_wait = time
        water_after_wait = water
        bought_after_wait = bought

        # pomijam pierwszy wierzcholek
        if v != s:
            # czekanie na nastepny autobus
            if time % OD[v] != 0:
                wait = OD[v] - (time % OD[v])
            else:
                wait = 0

            time_after_wait = time + wait
            if water - wait >= 0:
                #starczy wody
                water_after_wait = water - wait
            else:
                remaining_wait = wait - water
                bought_after_wait = bought + 1
                if b < remaining_wait:
                    continue
                water_after_wait = b - remaining_wait

        for u, w in G[v]:
            # sprawdzam czy moge dojechac bez wody
            if water_after_wait - w  >= 0:
                if d[u][water_after_wait - w] > bought_after_wait:
                    d[u][water_after_wait - w] = bought_after_wait
                    q.put((bought_after_wait,time_after_wait + w, water_after_wait - w,u))
            #dokupuje wode
            elif b - w >= 0:
                if d[u][b-w] > bought_after_wait + 1:
                    d[u][b -w] = bought_after_wait + 1
                    q.put((bought_after_wait + 1,time_after_wait + w, b-w, u))
            #wyjatek
            else:
                if d[u][0] > bought_after_wait + 1:
                    d[u][0] = bought_after_wait + 1
                    q.put((bought_after_wait + 1, time_after_wait + w, 0, u))
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