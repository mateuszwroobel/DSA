from kolutesty import runtests
from math import inf
from collections import deque


def swaps(disk, depends):
    deg = getdegree(depends)
    return BFS(disk, deg, depends)


def BFS(disk, deg, depends):
    n = len(depends)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    q = deque()
    for i in range(n):
        if not deg[i]:
            q.append(i)
            d[i] = 0
            visited[i] = True

    while q:
        v = q.popleft()
        if parent[v] is not None:
            if disk[parent[v]] != disk[v]:
                d[v] = d[parent[v]]+1
            else: d[v] = d[parent[v]]

        for u in depends[v]:
            deg[u] -= 1
            if deg[u] <= 0:
                if not visited[u]:
                    parent[u] = v
                    visited[u] = True
                    if disk[u] == disk[v]:
                        q.appendleft(u)
                    else:
                        q.append(u)

    return max(d)


def getdegree(depends):
    n = len(depends)
    deg = [0] * n
    for i, arr in enumerate(depends):
        for j in arr:
            deg[j] += 1
    return deg


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(swaps, all_tests=True)
