#Sorting "n" numbers from range n^2 - 1 in O(n) time
#Algortihm follow these steps
#Change base to "n"
# Use Radix Sort: Complexity of radix sort is O(d(n+k)), where "d" is max number of digit in number, k - base

def CountingSort(A,base,exp):
    n = len(A)
    C = [0 for _ in range(base)]
    B = [0 for _ in range(n)]
    for i in range(n):
        index = A[i] // exp % 10
        C[index] += 1
    for i in range(1,base):
        C[i] = C[i-1] + C[i]
    for i in range(n-1,-1,-1):
        index = A[i] // exp % 10
        C[index] -= 1
        B[C[index]] = A[i]
    for i in range(n):
        A[i] = B[i]

def Radixsort(A):
    max1 = max(A)
    exp = 1
    base = 10
    while max1 / exp >= 1:
        CountingSort(A,base,exp)
        exp *= 10

A = [45,23,78,97,123,9,12]
Radixsort(A)
print(A)

