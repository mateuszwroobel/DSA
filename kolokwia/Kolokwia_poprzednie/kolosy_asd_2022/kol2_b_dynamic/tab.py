from kol2btesty import runtests
from math import inf


def min_cost(O, C, T, L):
    n = len(O)
    A = [(0, 0)]  # Stacja A , (pozycja stacji, koszt zatrzymania)
    cost = [None for _ in range(n + 1)]
    # Tworzenie pomocniczych tablic
    for i in range(n):
        A.append((O[i], C[i]))
    A.sort()
    #A.append((L, 0))  # stacja B
    for i in range(n + 1):
        cost[i] = A[i][1]

    # F[i][0/1] - min koszt dojazdu do od i do n+1 uzywajac lub nie uzywajac wyjatku
    F = [[inf for _ in range(2)] for _ in range(n + 1)]
    F[n][1] = 0
    F[n][0] = 0
    for i in range(n,-1,-1):
        for u in range(0,2):
            if u == 1: #we can use our ability
                for j in range(i+1, n + 1):
                    if A[j][0] - A[i][0] > 2 * T:
                        break
                    #chcemy uzyc wyjatek w "i"
                    F[i][u] = min(F[i][u],  cost[i] + F[j][0])
                for j in range(i+1, n + 1):
                    if A[j][0] - A[i][0] > T:
                        break
                    #uzylismy gdzies pozniej
                    F[i][u]= min(F[i][u], cost[i] + F[j][1])
            else:
            #juz uzylismy wyjatek
                for j in range(i+1, n+1 ):
                    if A[j][0] - A[i][0] > T:
                        break
                    F[i][u] = min(F[i][u], cost[i] + F[j][0])

    return min(F[0])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)