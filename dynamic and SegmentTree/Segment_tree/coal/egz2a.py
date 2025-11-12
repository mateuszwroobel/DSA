from egz2atesty import runtests

#Rozwiazanie wykorzystuje implementacje drzewa o nastepujacej strukturze
#Liscie na samym poczatku maja wartosc "T", jest ich "n". Liscie reprezentuja kontenery
#Kazdy wewnetrzy wezel bedzie posiadal wartosc maximum z dwojga swoich dzieci.
#Taki sposob przechowywania wartosci mowi nam ile miejsca zostalo w kontenerze.
#Bedziemy przechodzic od korzenia do lisci idac z priorytetem w "lewo", tak aby
#byc zgodnym z naszym zadaniem:
#Zlozonosc O(nlogn)


def coal( A, T ):
    left = lambda i: 2*i + 1
    right = lambda i: 2*i + 2
    parent = lambda i: (i-1) //2

    class CoalContainer:
        def __init__(self,n,T):
            self.leaves = 1
            while self.leaves < n:
                self.leaves*=2

            self.heap = [0] * (2 * self.leaves  - 1)

            #prawdziwe kontenery, reszta lisci ma 0
            #pierwszy indeks liscia to self.leaves-1
            for i in range(n):
                self.heap[self.leaves - 1 + i] = T


            for i in range(self.leaves - 2, -1, -1):
                self.heap[i] = max(self.heap[left(i)], self.heap[right(i)])

        #O(logn)
        def update(self,i,val):
            k = i + self.leaves - 1
            #Umieszczam wegiel w magazynie "i" - odpowiednikiem w lisciu jest indeks "k"
            self.heap[k] -= val
            while k > 0:
                k = parent(k)
                self.heap[k] = max(self.heap[left(k)] ,self.heap[right(k)])

            #aktualizacja dla korzenia
            self.heap[0] = max(self.heap[left(0)], self.heap[right(0)])

        #O(logn)
        def find(self, node, coal_amount):
            #ide od korzenia w dol i szukam miejsca

            while node < self.leaves - 1:
                if coal_amount <= self.heap[left(node)]:
                    node = left(node)
                else:
                    node = right(node)
            #node - indeks w lisciach, przesuwam o self.leaves -1  aby uzyskac oryginalny
            return node - (self.leaves - 1)

    n = len(A)
    containers = CoalContainer(n,T)

    for i in range(n):
        ind = containers.find(0,A[i])
        last_idx = ind
        containers.update(ind,A[i])

    return last_idx

#O(n^2) - naive solution
# def coal( A, T ):
#     n =len(A)
#     m = [T for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if m[i] - A[j] >= 0:
#                 m[i]-=A[j]
#                 A[j] = 0
#                 if j == n-1:
#                     return i
#             else:
#                 continue
#     return

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True)
