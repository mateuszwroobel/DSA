# Mateusz Wróbel
'''Do policzenia inwersji w czasie nlogn wykorzystuje procedure merge, gdy podczas scalania liczba z prawej czesci
tablicy okaze sie mniejsza, wowczas zwiekszam inwersje o wszystkie elementy lewej tablicy - indeks i:
Zlozonosc czasowa nlogn
zlozonosc pamieciowa o(n)
gdzie n to dlugosc tablicy
'''

from zad2testy import runtests


def count_inversions(A):
    total_inv = 0
    total_inv += merge_sort(A, 0, len(A) - 1)
    return total_inv


def merge_sort(A, l, r):
    inv = 0
    if l < r:
        mid = (r + l) // 2
        inv += merge_sort(A, l, mid)
        inv += merge_sort(A, mid + 1, r)
        inv += merge_and_count(A, l, r)
    return inv


def merge_and_count(A, l, r):
    mid = (r + l) // 2
    left = A[l:mid + 1]
    right = A[mid + 1:r + 1]
    i = j = 0
    k = l
    inv = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            inv += len(left) - i
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    return inv

# Odkomentuj by uruchomic duze testy
# runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( count_inversions, all_tests=True )
