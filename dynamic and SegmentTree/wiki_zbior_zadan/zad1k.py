from zad1ktesty import runtests

def roznica( S ):
    n = len(S)
    K = [0] * n
    for i in range(n):
        if S[i] == "1":
            K[i] = -1
        else:
            K[i] = 1

    #Kadane alg
    dp = [0] * n
    best = dp[0]
    dp[0] = max(0,K[0])
    for i in range(1,n):
        dp[i] = max(dp[i-1] + K[i], 0)
        best = max(best,dp[i])

    return best if best != 0 else -1

runtests ( roznica )