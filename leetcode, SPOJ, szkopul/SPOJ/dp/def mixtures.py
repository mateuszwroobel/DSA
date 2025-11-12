def mixtures(colors,n):
    inf = float('inf')
    dp = [[inf for _ in range(n)] for _ in range(n)]
    #f(i,j) - najmniejszy dym dla przedzialu i,j
    #sa dwie mozliwosci albo mnoze element z lewej albo z prawej
    #prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + colors[i]

    sums = [[0 for _ in range(n)] for _ in range(n)]

    #suma dla kadego przedzialu (i,j)
    for i in range(n):
        for j in range(i,n):
            sums[i][j] = (prefix[j + 1] - prefix[i]) % 100

    def f(i,j):
        if i == j: return 0
        if dp[i][j] != inf: return dp[i][j]
        dp[i][j] = min(sums[i][k] * sums[k+1][j] + f(i,k) + f(k+1,j) for k in range(i,j))
        return dp[i][j]


    return f(0,n-1)

A =[40,60,20]
print(mixtures(A,len(A)))
