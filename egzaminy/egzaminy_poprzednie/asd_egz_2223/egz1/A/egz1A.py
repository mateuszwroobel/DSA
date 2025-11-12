from egz1Atesty import runtests
from queue import PriorityQueue
from math import inf


def gold(G, V, s, t, r):
    # zmodyfikowany algorytm dijktry ktory bedzie sledzil czy juz ukradl
    # i z ktorego zamku ukradl aby, w taki sposob policzy sciezke o najmniejszym koscie
    # musze miec indeks v z ktorego ukradl, gdybym sledzil tylko czy ukradl, to algorytm rozpatrywalby tylko to ze ukradl z pierwszego napotkanego
    # zmodyfikowana dijkstra
    n = len(G)
    # d[v][k] - najmniejszy koszt do "v" z ukradzionymi pieniedzmi z "k", dodajac narazie rabunku
    d = [[inf] * 2 for _ in range(n)]  # #0 - nie obraborwano , 1 obrabowano
    q = PriorityQueue()
    q.put((0, s, 0))  # dist, v ,
    d[s][0] = 0
    while not q.empty():
        cost, v, robbed = q.get()
        if cost > d[v][robbed]:
            continue
        if robbed == 0:
            robbery_cost = cost - V[v]
            if robbery_cost < d[v][1]:
                d[v][1] = robbery_cost
                q.put((robbery_cost, v, 1))
        for u, w in G[v]:
            if robbed != 0:
                if d[u][1] > cost + w * 2 + r:
                    d[u][robbed] = cost + w * 2 + r
                    q.put((cost + w * 2 + r, u, 1))
                    # print(f"do kolejki {d[u][robbed]}: {u}: robbed:{robbed}")
            else:
                if d[u][0] > cost + w:
                    d[u][0] = cost + w
                    q.put((cost + w, u, 0))
    min_cost = min(d[t][0], d[t][1])
    return min_cost


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
