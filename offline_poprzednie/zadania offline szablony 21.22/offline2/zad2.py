from zad2testy import runtests
#nlogn to przedzialowka
def depth(T):
    n = len(T)
    T = [(min(x,y), max(x,y)) for x,y in T]
    T = sorted(T, key=lambda x: (x[0],-x[1]))
    A = [-y for x,y in T]

    def binary_search(arr, l, p , x):
        while l < p:
            mid = (l+p)//2
            if arr[mid] < x:
                l = mid + 1
            else:
                p = mid
        return l

    lis = [A[0]]
    for i in range(1,n):
        k = len(lis)
        last = lis[-1]
        if A[i] > last:
            lis.append(A[i])
        else:
            index = binary_search(lis,0,k,A[i])
            lis[index] = A[i]

    return len(lis)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
# runtests(all_tests=True )

runtests(depth)
