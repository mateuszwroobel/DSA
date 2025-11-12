# Mateusz Wróbel
'''
Liczby ukladaja sie zgodnie z rozkladem jednostajnym, dlatego stosuje algorytm bucketsort wraz
z mergem sortem w pojedynczym kubelku. Dziele przedzial na M bucketow i sortuje liczby w kazdym
z bucketow. Pozniej sklejam wszystkie buckety razem co powoduje ze liczby w calej tablicy sa posortowane.
Nastepnie przechodze po posortowanej tablicy i sprawdzam czy odleglosc miedzy dwoma
kolejnymi palikami jest wieksza lub rowna niz szerokosc kombajna. Gdy warunek jest spelniony
zwiekszam licznik wjazdow na pole.

Zlozonosc czasowa sortowania jednym buckecie: O(1/Mlog1/M)
sklejanie bucketow: O(M)
Sprawdzanie miedzy palikami: 0(2N)

Zlozonosc pamieciowa tworzenia bucketow O(M)
'''
from kol1testy import runtests


def ogrodzenie(M, D, T):
    n = len(T)
    A = bucket(M, D, T)
    counter = 0
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        if diff >= D:
            counter += 1
    return counter


def bucket(M, D, T):
    n = len(T)
    buckets = [[] for i in range(M)]
    for i in range(n):
        number = int(T[i] / n)
        buckets[number].append(T[i])
    for b in buckets:
        insertionSort(b)
    A = [0 for i in range(n)]
    i = 0
    for b in buckets:
        if len(b) != 0:
            for letter in b:
                A[i] = letter
                i += 1
                x
    return A


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ogrodzenie, all_tests=True)
