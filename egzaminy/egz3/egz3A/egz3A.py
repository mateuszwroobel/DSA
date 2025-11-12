from egz3Atesty import runtests

# Rozwiazanie bedzie korzystalo z drzewa przedzialowego.
# Jednak najpierw nalezy skompresowac wysokosci drzew do wartosci 0 do n-1 aby mozna uzyc drzewa przedzialowego, ktorego
# liscie beda licznikami wartosci


def treecut(H, k):
    #funkcja kompresujaca punkty
    def compress(A):
        mapped = { v : index for index,v in enumerate(sorted(A)) }
        #klucz - oryginalny punkt
        #index - skompresowany punkt
        return mapped

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

        def update(self,i):
            #Aktualizacja wartosci
            #Parametry:
            #i - oryginalny indeks w  tablicy

            #Szukam liscia o odpowiedniku "i"
            q = i + self.leaves - 1

            #Wedrujemy od liscia do korzenia
            while q > 0:
                self.heap[q] += 1
                q = parent(q)
            self.heap[0] += 1

        def _sum(self,node, n_low, n_high, i, j):
            # Suma w przedziale i-j:
            # node odpowiada za sume przedziale od n_low - n_high
            # czyli de-facto ile jest liczb z przedzialu od n_low - n_high

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


    mapped = compress(H)
    n = len(H)
    st = SegmentTree(n)
    impossible = 0
    for i in range(n):
        tree = mapped[H[i]]
        impossible += st.sum(tree+1,n)
        if impossible > k:
            return i
        st.update(tree)
    return n


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(treecut, all_tests=True)
