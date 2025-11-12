from kol2btesty import runtests
from math import inf
from heapq import heappush, heappop

def min_cost(O, C, T, L):
    n = len(O)
    m = n+1
    A = [(0, 0)]  # Stacja A , (pozycja stacji, koszt zatrzymania)
    cost = [0] * m #koszt
    P = [0] * m # stacja
    # Tworzenie pomocniczych tablic
    for i in range(1,m):
        A.append((O[i-1], C[i-1]))
    A.sort()
    for i in range(1,m):
        cost[i] = A[i][1]
        P[i] = A[i][0]
    heap_max = []
    heap_min = []
    # F[i][0/1] - min koszt dojazdu do od i do m uzywajac(1) lub nie uzywajac wyjatku(0)
    F = [[inf for _ in range(2)] for _ in range(m)]
    F[n][1] = 0
    F[n][0] = 0
    for i in range(m-1,-1,-1):
        for u in range(0,2):
            #mozemy uzyc wyjatku
            if u == 1:
                for j in range(i+1, m):
                    if P[j] - P[i] > 2 * T:
                        break
                    #chcemy uzyc wyjatek w "i"
                    F[i][u] = min(F[i][u],  cost[i] + F[j][0])
                for j in range(i+1, m):
                    if P[j] - P[i] > T:
                        break
                    #uzylismy gdzies pozniej
                    F[i][u]= min(F[i][u], cost[i] + F[j][1])
            else:
            #juz uzylismy wyjatek
                for j in range(i+1,m):
                    if P[j]- P[i] > T:
                        break
                    F[i][u] = min(F[i][u], cost[i] + F[j][0])

    return min(F[0])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)