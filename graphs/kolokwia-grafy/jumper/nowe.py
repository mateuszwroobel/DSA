from zad6testy import runtests
from queue import PriorityQueue
from math import inf


def jumper(G, s, w):
    return jumper_dijkstra(g,s,w)


def jumper_dijkstra(G, s, t):
    n = len(G)
    d = [[inf for _ in range(3)]  for _ in range(n)]
    # 1 - zaczynam uzywac
    # 0 - nie mozemy uzyc
    # d[v][2]- dopiero uzyto (pozwoli nam to wybrac wage)/ wierzcholek pomiedzy
    q = PriorityQueue()
    d[s][0] = 0
    q.put((0, s, 1, 0))  # time, v, id, waga z jaka wchodzilem do wieczholka
    while not q.empty():
        time, v, id ,weight_in = q.get()
        for u, w in G[v]:
            if d[u][id] > time + w:
                d[u][id] = time + w
                q.put((time+w,u,id,w))
        if id == 0:
            #jezeli nie mozemy uzyc butow patrze czy aktualned d[u][1] jest lepsze niz d[v]
            for u,w in G[v]:
                if d[u][id + 1] > time + w:
                    d[u][id + 1] = time + w
                    q.put((time+w,u,id+1,w))
        elif id == 1:
            for u,w in G[v]:
                if d[u][id + 1] > w + time:
                    d[u][id + 1] = w + time
                    q.put((w+time,u,id+1,w))
        elif id == 2:
            for u,w in G[v]:
                maks = max(weight_in, w)
                mini = min(weight_in,w)
                if d[u][0] > maks + time - mini:
                    d[u][0] = maks + time - mini
                    q.put((maks+time-mini,u,0,maks))

    return min(d[t][0],d[t][1],d[t][2])


runtests(jumper, all_tests=True)
