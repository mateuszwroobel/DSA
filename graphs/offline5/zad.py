from collections import deque

from zadtesty import runtests
from math import inf
from queue import PriorityQueue


def goodknight(G, s, t):
    d = matrix_to_adj(G,len(G))
    return bfs(d,s,t)

def bfs(G, s, t):
    #
    n = len(G)
    distance       = [ [ float('inf') for _ in range(17) ] for _ in range(n) ]
    distance[s][0] = 0
    queue    = deque()
    queue.appendleft( (s, 0, 0) )

    while queue:
        vertex, value, time = queue.popleft()

        if value > 0: queue.append( (vertex, value - 1, time) )
        else:

            for neighbour, weight in G[vertex]:

                if distance[vertex][time] + weight + 8 < distance[neighbour][weight]:
                    distance[neighbour][weight] = distance[vertex][time] + weight + 8
                    queue.append( (neighbour, weight, weight) )

                if time + weight <= 16:
                    if distance[vertex][time] + weight < distance[neighbour][time + weight]:
                        distance[neighbour][time + weight] = distance[vertex][time] + weight
                        queue.append( (neighbour, weight, time + weight) )

            #end 'for' clause
        #end 'if' clause
    #end 'while' loop

    return min( distance[t] )


def matrix_to_adj(G, n):
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                g[i].append((j, G[i][j]))
    return g


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
