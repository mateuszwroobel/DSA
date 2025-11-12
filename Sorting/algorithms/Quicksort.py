def partition(A,p,r):
    n = len(A)
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

A = [4,2,1,5,2,7,8,9]
quicksort(A,0,len(A)-1)
print(A)