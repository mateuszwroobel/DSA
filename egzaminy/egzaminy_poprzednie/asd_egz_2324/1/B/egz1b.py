from egz1btesty import runtests
from math import inf

def kstrong(T, k):
    n = len(T)
    F = [[0 for _ in range(k+1)]for _ in range(n)]
    best = 0
    #czy sie oplaca usuwac pierwszy element
    for j in range(k+1):
        F[0][j] = max(0,T[0])
    #pierwsza kolumna
    for i in range(n):
        F[i][0] = max(T[i], F[i-1][0] + T[i])
    for i in range(1,n):
        for j in range(1,k+1):
            F[i][j] = max(F[i-1][j] + T[i],  F[i-1][j-1])
            best = max(best, F[i][j])
    return best

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
