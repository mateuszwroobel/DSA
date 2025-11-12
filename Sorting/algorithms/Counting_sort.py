def CountingSort(A,k):
    n = len(A)
    C = [0 for _ in range(k+1)]
    B = [0 for _ in range(n)]
    for i in range(n):
        C[A[i]] += 1
    for i in range(1,k+1):
        C[i] = C[i-1] + C[i]
    for i in range(n-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]

A = [3,2,3,4,1,2,2,6,2,3,1,5]
CountingSort(A,max(A))
print(A)
