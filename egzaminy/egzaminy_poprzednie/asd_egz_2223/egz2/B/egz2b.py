from egz2btesty import runtests
from math import inf

def parking(X, Y):
    m = len(Y)
    n = len(X)

    dp = [[inf for _ in range(m)] for _ in range(n)]
    #base case
    #parkuje pierwszy samochod
    for j in range(0,m):
        dp[0][j] = abs(X[0] - Y[j])

    for i in range(1, n):
        best_previous_park = inf
        for j in range(m):
            dp[i][j] = min(dp[i][j], best_previous_park + abs(X[i] - Y[j]))
            best_previous_park = min(dp[i-1][j], best_previous_park)

    return min(dp[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
