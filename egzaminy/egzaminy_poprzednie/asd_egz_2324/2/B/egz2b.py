from egz2btesty import runtests
from collections import deque
from math import inf

#przyladkowa - 10 minut typ1
#indyjska - 5 minut typ2
#zmiana to 20 minut
#d[v] - czas po ktorym wyjedziemy ze stacji, w przypadku gdy
#"v" jest rozne niz stacja koncowa, gdy v == B, wtedy nie licze po zamainie
def tory_amos(E, A, B):
    G = adj_to_edge(E)
    time = modified_dijkstra(G,A,B)
    return time

def modified_dijkstra(G,s,t):
    n = len(G)
    d = [[inf] * 2 for _ in range(n)]
    d[s][0] = 0
    d[s][1] = 0
    q = deque()
    q.append((0,s,None,0)) #dist, v, dowolne, delay
    while q:
        dist, v, typ_in, delay  = q.popleft()
        if n  == 6:
            print(f"jestem w : {v}, czas: {dist}, delay: {delay}")
        if delay > 0:
            q.append((dist,v,typ_in,delay-1))
            continue
        # na poczatku tory sa przystosowane
        if v == s:
            for u,w,typ in G[v]:
                if d[u][typ] > w:
                    d[u][typ] = w
                    q.append((w,u,typ,w))
            continue
        if dist > d[v][typ_in]:
            continue
        for u,w,typ in G[v]:
            if typ_in != typ:
                time_in_station = 20
            elif typ == 1:
                time_in_station = 10
            else:
                time_in_station = 5
            #czas odjazdu se stacji
            new_dist = dist + time_in_station + w
            if d[u][typ] > new_dist:
                d[u][typ] = new_dist
                q.append((new_dist,u,typ,w))
    return min(d[t])

def adj_to_edge(E):
    n = max(max(u,v) for u,v,w,t in E) + 1
    G = [[] for _ in range(n)]
    for u,v,w,t in E:
        if t == 'P':
            typ = 1
        else:
            typ = 0
        G[u].append((v, w, typ))
        G[v].append((u, w, typ))
    return G


runtests(tory_amos, all_tests=True) # Run only basic tests first