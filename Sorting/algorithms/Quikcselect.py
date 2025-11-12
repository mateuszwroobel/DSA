def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] >= x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def Quick_select(A,p,r,k):
    if p  == r:
        return A[p]
    q = partition(A,p,r)
    if q == k-1:
        return A[q]
    elif q>k-1:
        return Quick_select(A,p,q-1,k)
    else:
        return Quick_select(A,q+1,r,k)

A = Quick_select([4,2,1,6,3,9,7],0,6,0)
print(A)

