from egzP6atesty import runtests 

def google (H, s):
    n = len(H)
    #Tworze tablice T, ktora bedzie sie skladac krotek (dlugosc, liczba_liter, haslo)
    T = [0 for _ in range(n)]
    for i in range(n):
        T[i] = (len(H[i]),count_letters(H[i]),H[i])
    quicksort(T,0,len(T)-1)
    return T[s-1][2]

def count_letters(string):
    c = 0
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            c+=1
    return c

def median_of_three(A, p, r):
    mid = (p + r) // 2
    if A[p] > A[mid]:
        A[p], A[mid] = A[mid], A[p]
    if A[p] > A[r]:
        A[p], A[r] = A[r], A[p]
    if A[mid] > A[r]:
        A[mid], A[r] = A[r], A[mid]
    A[mid], A[r] = A[r], A[mid]


def partition(A,p,r):
    n = len(A)
    median_of_three(A,p,r)
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] > x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

runtests ( google, all_tests=True )