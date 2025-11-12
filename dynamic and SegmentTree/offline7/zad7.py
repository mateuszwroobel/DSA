from zad7testy import runtests
from math import inf


def orchard(T, m):
    # F[i][k] - ile minimalnie drzew z "i" pierwszych, trzeba wyciac aby suma na pozostawionych dawala reszkte k
    n = len(T)
    F = [[inf for _ in range(m)] for _ in range(n)]
    cut_first = T[0] % m
    F[0][0] = 1
    F[0][cut_first] = 0
    for i in range(1, n):
        for k in range(m):
            F[i][k] = min(F[i][k], F[i - 1][k] + 1) #wycinamy
            new_k = (k + T[i]) % m
            F[i][new_k] = min(F[i][new_k], F[i - 1][k]) #zostawiamy

    return F[n - 1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
