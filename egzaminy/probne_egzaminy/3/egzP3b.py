from egzP3btesty import runtests 
from queue import PriorityQueue
from math import inf
def lufthansa ( G ):
    return kruskal(G)

class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank+=1
    return True

def sort_edge(G):
    n = len(G)
    done = [False for _ in range(n)]
    E = []
    sum_weight = 0
    for i in range(n):
        for u,w in G[i]:
            if not done[u]:
                E.append((i,u,w))
                sum_weight+=w
        done[i] = True
    E = sorted(E, key = lambda x : x[2],reverse=True)

    return E,sum_weight

def kruskal(G):
    n = len(G)
    nodes = [Node(i) for i in range(n)]
    E,sum_weight = sort_edge(G)
    mst =[] #max spanning tree
    maks = -inf
    sum = 0
    for u,v,w in E:
        if union(nodes[v],nodes[u]):
            sum+=w
        else:
            maks = max(maks,w)
    return sum_weight - sum - maks
runtests ( lufthansa, all_tests=True )