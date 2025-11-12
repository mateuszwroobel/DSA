from zad9testy import runtests
from math import inf


def trip(M):
    n = len(M)
    m = len(M[0])
    F = [[-inf for _ in range(m)] for _ in range(n)]
    def reku(i, j):
        if i > n - 1 or j > m - 1 or i < 0 or j < 0: return -inf
        if F[i][j] != -inf: return F[i][j]

        neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        T = [reku(neighbors[k][0],neighbors[k][1]) for k in range(4)
                      if 0 <= neighbors[k][1]  < m
                      and   0 <= neighbors[k][0]  < n
                      and M[neighbors[k][0]][neighbors[k][1]] > M[i][j]]
        if T:
            F[i][j] = max(T) + 1
        else:
            F[i][j] = 1 #gdy nie ma dalej przejscia oznacza ze jest to start

        return F[i][j]

    best = -inf
    for i in range(n):
        for j in range(m):
            best = max(best,reku(i,j))
    return best

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
