def largest_divisible_subset(A):
    # f(i) - najdluzszy podciag, konczace sie na i
    n = len(A)
    dp = [1] * n
    parent = [None] * n
    last = 0
    A.sort()
    for i in range(n):
        for j in range(i):
            if A[i] % A[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    #find last_element
    maxi = max(dp)
    for ind, x in enumerate(dp):
        if x == maxi:
            last = ind
            break
    def recontruct(last, dp):
        path = []
        while last is not None:
            path.append(A[last])
            last = parent[last]

        return path

    return recontruct(last,dp)

print(largest_divisible_subset([3,4,16,8]))



