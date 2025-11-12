#Implementacja struktury danych, która pozwala wykonywac nastepujace operacje:
#Dodawanie elementów tablicy w czasie O(log(n)):
#Modyfikacja elementow w tablicy w czasie O(log(n)):

left = lambda i: i*2 + 1
right = lambda i: i*2 + 2
parent = lambda i: (i-1)//2

class SegmentTree:
    def __init__(self,n):
        self.leaves = 1

        #Liscie to elementy naszej oryginalnej tablicy
        #Wezly wewnetrze to sumy przedzialow
        while self.leaves < n:
            self.leaves*=2

        #Drzewo binarne ma 2*(liczba lisci) - 1 wezlow
        #Liscie zaczynaja sie od indeksu (leaves - 1)
        self.heap = [0] * (2*self.leaves - 1)

    def update(self,i,val):
        #Aktualizacja wartosci
        #Parametry:
        #i - oryginalny indeks w  tablicy
        #val - wartosc, ktora chcemy wstawic

        #Szukam liscia o odpowiedniku "i"
        k = i + self.leaves - 1
        diff = val - self.heap[k]

        #Wedrujemy od liscia do korzenia
        while k > 0:
            self.heap[k] +=diff
            k = parent(k)
        self.heap[0] += diff

    def _sum(self,node, n_low, n_high, i, j):
        # Suma w przedziale i-j:
        # node odpowiada za sume przedziale od n_low - n_high

        #Case 1 - Przedzialy nie nachodza na siebie
        if n_low > j or n_high  < i:
            return 0
        #Case 2 - Przedzial za ktory odpowiedzialny jest node zawiera sie w calosci
        if n_low >= i and n_high <= j:
            return self.heap[node]

        #Case 3 - Przedzialy sie przecinaja
        mid = (n_low+n_high)//2
        sum_left = self._sum(left(node),n_low,mid,i,j)
        sum_right = self._sum(right(node),mid+1,n_high,i,j)
        return sum_left + sum_right

    def sum(self,i,j):
        return self._sum(0, 0, self.leaves-1, i, j)

#
#
# arr = [1,3,2,4,1,7,3,6]
#
# tree = SegmentTree(len(arr))
# for i in range(len(arr)):
#     tree.update(i,arr[i])
#
# print(tree.sum(1,4))
