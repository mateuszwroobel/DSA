def subarray_sum(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][i] = A[i]  # Suma jednego elementu
        for j in range(i + 1, n):
            F[i][j] = F[i][j - 1] + A[j]
    print(F)

A = [2,3,1,10,65,1]
subarray_sum(A)