def rock(A,n):
    inf = float('inf')
    #okreslam funkcje rekurencyjna:
    #f(i,j) - suma dlugosci fragmentow ktore mozna pociac dla przedzialu A[i...j]
    dp = [[-inf for _ in range(n)] for _ in range(n)]

    #sprawdzam czy bede mogl pociac dany przedzial
    sums = [[0 for _ in range(n)]for _ in range (n)]
    can_cut = [[False for _ in range(n)]for _ in range (n)]

    #base case
    for i in range(n):
        dp[i][i] = A[i]

    #prefix sum
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + A[i]

    #sum for each (i,j)
    for i in range(n):
        for j in range(i,n):
            sums[i][j] = prefix[j+1] - prefix[i]
            if sums[i][j] > (j-i+1)//2:
                can_cut[i][j] = True

    def f(i,j):
        if i < 0 or j < 0: return 0
        if dp[i][j] != -inf: return dp[i][j]
        if can_cut[i][j]:
            len_of_fragment = j-i+1
            dp[i][j] = len_of_fragment
            return len_of_fragment
        else:
            dp[i][j] = max(f(i,k) + f(k+1,j) for k in range(i,j))

        return dp[i][j]

    return f(0,n-1)

A = [0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0]
print(rock(A,len(A)))