from email.policy import default
from math import inf
from queue import PriorityQueue
import heapq



def findCheapestPrice(n, E, s, t, k):
    def edge_to_adj(E,n):
        G = [[] for _ in range(n)]
        for v,u,w in E:
            G[v].append((u,w))
        return G
    G = edge_to_adj(E,n)

    d = [[inf]*(k+2) for _ in range(n)]
    d[s][0] = 0
    q = PriorityQueue()
    q.put((0,s,0)) #vertex, time, stops
    while not q.empty():
        time,v,stops = q.get()
        if time > d[v][stops]:
            continue
        if v == t:
            return time
        for u,w in G[v]:
            if stops <= k:
                new_time = time + w
                if d[u][stops+1] > new_time:
                    d[u][stops+1] = new_time
                    q.put((new_time,u,stops+1))

    return min(d[t])

#882
def reachableNodes(edges, maxMoves,n):
    def create_weighted_graph(edges,n):
        #rozczepianie krawedzi mozna potraktowac jako krawedz wazona
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w+1))
            g[v].append((u, w+1))
        return g

    g = create_weighted_graph(edges,n)
    cnt = 0

    d = [float('inf')] * n
    d[0] = 0
    heap = [(0,0)] #dist, v
    while heap:
        dist, v = heapq.heappop(heap)
        if dist > d[v]:
            continue
        for u,w in g[v]:
            new_cost = dist + w
            if new_cost < d[u]:
                d[u] = new_cost
                heapq.heappush(heap,(new_cost,u))

    #zliczanie oryginalnych wierzcholkow
    for dist in d:
        if dist <= maxMoves:
            cnt+=1
    for u,v,w in edges:
        #z jednej strony
        nodes_from_u = max(maxMoves - d[u],0)
        #z drugiej strony
        nodes_from_v = max(maxMoves - d[v],0)
        cnt += min(w,nodes_from_u + nodes_from_v) #potrzebna waga, zeby nie przekroczyc
    return cnt

# edges = [[0,1,10],[0,2,1],[1,2,2]]; maxMoves = 6; n = 3
# print(reachableNodes(edges,6,3))

#2045
def secondMinimum(n, edges, w, change):
    def create_graph(n, edges, w):
        G = [[] for _ in range(n + 1)]
        for u, v in edges:
            G[u].append((v, w))
            G[v].append((u, w))
        return G

    G = create_graph(n, edges, w)
    heap = []
    heapq.heappush(heap, (0, 1))  # time, v
    dist = {}
    visited = 0  # ile razy odwiedzalismy wierczholek "n"

    while heap:
        time, v = heapq.heappop(heap)
        if v == n:
            visited += 1
            if visited == 2:
                # dotarlismy drugi raz do wierzcholka "n",
                # to oznacza ze mamy policzony drugi najlepszy czas
                return time

        light = (time // change) % 2
        # 0 - zielone
        # 1 - czerwone
        if light == 0:
            time_till_depart = 0
        else:
            # czas do odjazdu
            time_till_depart = change - (time % change)

        for u, w in G[v]:

            # czas przybycia do nastepnego wierzcholka to
            # aktualny czas podrozy + czas do zielonego swiatla + dystans
            arrival_time = time + time_till_depart + w

            if arrival_time < dist.setdefault((u, arrival_time), float('inf')):
                dist[(u, arrival_time)] = arrival_time
                heapq.heappush(heap, (arrival_time, u))

    return -1


# n = 5; edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]; time = 3; change = 5
# #n = 2; edges = [[1,2]]; time = 3; change = 2
# print(secondMinimum(n,edges,time,change))

#2203
'''Uruchamiam dijkstre 3 razy: z s1 i s2, i z dest na odwroconym grafie
teraz dla kazdego wierzcholka "v" obliczam sciezke:
sciezka to: 
oznaczenia d(u,v) - odleglosc miedzy u i v
d(s1,v) + d(s2,v) + d(dest,v) 
szukam minimalnej wartosci takiej sciezki, co mi da ostateczna odpowiedz:
Ten sposob dziala takze gdy "v" to s1 lub s2, wtedy sciezka przechodzi odpowiednio przez 
jeden z wierzcholkow,
'''
def minimumWeight(n, edges, s1, s2, dest):


    def create_weighted_graph(edges,n):
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w))
        return g
    def create_graph_from_dest(edges,n):
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[v].append((u, w))
        return g

    g = create_weighted_graph(edges,n)
    g_dest = create_graph_from_dest(edges,n)

    def dijkstra(n,g,s):
        d = [float('inf')] * n
        d[s] = 0
        heap = [(0,s)] # dist, v
        while heap:
            dist, v = heapq.heappop(heap)
            if dist > d[v]:
                continue
            for u,w in g[v]:
                new_cost = dist + w
                if new_cost < d[u]:
                    d[u] = new_cost
                    heapq.heappush(heap,(new_cost,u))
        return d

    from_d1 = dijkstra(n,g,s1)
    from_d2 = dijkstra(n,g,s2)
    from_dest = dijkstra(n,g_dest,dest)
    if from_d1[dest] == float('inf') or from_d2[dest] == float('inf'):
        return -1

    #szukam najlepszego wierzcholka przez ktory trzeba isc
    best = float('inf')
    for v in range(n):
        path = from_d1[v] + from_d2[v] + from_dest[v]
        best = min(best,path)
    return best
# n = 6; edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]; src1 = 0; src2 = 1; dest = 5
# print(minimumWeight(n, edges, src1, src2, dest))