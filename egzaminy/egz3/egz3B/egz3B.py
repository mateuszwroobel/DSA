from egz3Btesty import runtests
def kom(X, Z, W):
    n = len(X)
    dp = [[-1 for _ in range(W+1)] for _ in range(n)]
    #base case
    #nic nie rob
    dp[0][W] = 0
    if W - Z[0] >= 0: #wyscig
        dp[0][W - Z[0]] = max(dp[0][W - Z[0]], X[0])
    for i in range(1,n):
        for z in range(W,-1,-1):
            dp[i][z] = dp[i-1][z]
            if z >= Z[i]:
                spa = dp[i-1][z-Z[i]] - X[i]
                if spa > 0:
                    dp[i][z] = max(dp[i][z], spa)

            if z+Z[i] <= W and dp[i-1][z+Z[i]] != -1:
                race = dp[i-1][z+Z[i]] + X[i]
                dp[i][z] = max(dp[i][z], race)

    return max(dp[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kom, all_tests=True)
