#Mateusz Wróbel
from zad8testy import runtests
from math import inf


def parking(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[inf] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = abs(X[0] - Y[j])

    for i in range(1, n):
        for j in range(m):
            for k in range(i-1,j):
                dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(X[i] - Y[j]))

    return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
