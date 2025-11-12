from kolUtesty import runtests

'''
O(nk)
Opis algorytmu:
Na poczatku zliczam wystapienia kazdej liczby w tablicy T. Pozniej w pomoczniczej  tablicy dla kazdeo elementu w tablicy T iteruje
w zakresie j w zakresie od 0 do T[i] bo liczby wieksze po prawej stronie mnie nie interesuja, w pomocniczej tablicy mam zapisane ile elementow juz minalem.
W tablicy C mam informacje ile elementow jest w calej tablicy. To oznacza ze C[j] - help[j] da nam odpowidz ile jest elementow mniejszych po prawej stronie. 
Przyklad:
A = [1,2,2,1,1]
i = 1
j = 1
aktualny help: [0,1,1] (zaczynam od 0, help[0] = ile zer minalem)
C = [0,3,2]
Patrze na dwojke i wiem ze minalem juz jedna jedynke, co wiecej wiem ile mam w calej tablicy (3) wiec obliczam ile mam po prawej stronie od tej dwojki (3-1)
'''


def kawa(T, k):
    n = len(T)
    C = [0] * (k+1)
    coffee = 0

    for i in range(n):
        C[T[i]] += 1

    help = [0] * (k+1)
    for i in range(n):
        #tablica help mowi mi ile napotkalem cyfr do indeksu i
        help[T[i]] += 1
        for j in range(T[i]):
            #help[j] - tyle liczb "j" mam po lewej stronie
            #C[j] tyle liczb mam "j" w calej tablicy
            #Zliczam ile liczb jest mniejszych od T[i] po prawej stronie
            coffee+= C[j] - help[j]

    return coffee

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kawa, all_tests=True)
