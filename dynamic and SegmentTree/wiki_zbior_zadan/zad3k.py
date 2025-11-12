from zad3ktesty import runtests
from math import inf

def ksuma( T, k ):
    n = len(T)
    dp = [inf for _ in range(n)]
    for i in range(k):
        dp[i] = T[i]
    for i in range(k,n):
        for j in range(i-k,i):
            dp[i] = min(dp[i], dp[j] + T[i])
    return min(dp[n-k:n])
runtests ( ksuma )