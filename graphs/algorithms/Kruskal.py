G = [ [(1,3), (2,1), (4,2)],
[(0,3), (2,5) ],
[(1,5), (0,1), (3,6)],
[(2,6), (4,4) ],
[(3,4), (0,2) ] ]

#find-union structure

class node:
    def __init__(self,val):
        self.parent = self
        self.rank = 0
        self.val = val

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

def sort_edges(G):
    n = len(G)
    done = [False for _ in range(n)]
    E = []
    for i in range(n):
        for u,w in G[i]:
            if not done[u]:
                E.append((i,u,w))
        done[i] = True
    E = sorted(E, key=lambda x: x[2])
    return E

def kruskal(G):
    n = len(G)
    mst = []
    E = sort_edges(G)
    nodes = [node(i) for i in range(n)]
    for u,v,w in E:
        if union(nodes[u],nodes[v]):
            mst.append((u,v,w))
    return mst

print(kruskal(G))

