# O(n^2)
def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    return max(F)


# O(nlogn)
def lis_with_binary_search(A):
    global k
    n = len(A)
    res = [A[0]]
    for i in range(1,n):
        k = len(res)
        last = res[k-1]
        if A[i] > last:
            res.append(A[i])
        else:
            index = lower_bound(res,0,k, A[i])
            res[index] = A[i]

    return k


def lower_bound(A, l, r, x):
    while l < r:
        mid = (l+r)//2
        if A[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l


