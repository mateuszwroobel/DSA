def most_exp_common_subsequence(n,m,A,B,price):
    #f(i,j) - najdluzszy wspolny podciag dla tablicy A[....i] i B[0...j]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                cost = price[ord(A[i-1])]
                dp[i][j] = dp[i-1][j-1] + cost + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[m][n]