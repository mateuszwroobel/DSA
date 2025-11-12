from kolUtesty import runtests


#Do rozwiazania wykorzystuje drzewo przedziałowe:
#Liscie drzewa beda posiadaly liczniki wartosci. Np pierwszy lisc to liczba zer w dotyczasowo rozwazanym przedziale
#Kazdy wezel przechowuje informacje o sumie czyli liczebnosci wartosci w danym przedziale:
# np wezel ktory odpowiada za przedzial 0-4 przechowuje liczbe zer,jedynek,dwojek,czworek w dotyczchasowo napotkanej tablicy.
#Bede szedl od konca i dla kazdego T[i] bede zliczal ile jest wartosci od 0 do T[i-1] w drzewie:
#sum (0,T[i-1])
#na koniec dodam T[i]do drzewa, czyli bede wedrowal od liscia w gore i zwiekszal wartosci o 1


def kawa(T, k):
    left = lambda i: 2*i+1
    right = lambda i: 2*i + 2
    parent = lambda i: (i-1)//2

    class SegmentTree:
        def __init__(self,n):
            self.leaves = 1
            while self.leaves < n:
                self.leaves*=2

            self.heap = [0] * (2*self.leaves - 1)


        def update(self,value):
            #parameter value - wartosc ktorej zwiekszam liczebnosc
            #szukam liscia ktory zlicza ile jest "value" i wedruje w gore dodajac "1"
            #liscie zaczynaja sie od self.leaves - 1
            value += self.leaves - 1
            #wedrowanie w gore
            while value > 0:
                self.heap[value] +=1
                value = parent(value)

            #aktualizacja dla korzenia
            self.heap[value] += 1

        def _sum(self,node,node_low,node_high,i,j):
            #parametry:
            #node - akutalnie rozwazany wezel
            #node_low, node_high - przedzial, za ktory odpowiedzialny jest wezel np: korzen jest odpowiedzialny za cala tablice (0,self.leaves -1)
            #i,j - suma przedzialu i-j, ktorej szukamy (u nas odpowiada liczebnosci liczb od i do j)

            #case 1: Przedzialy sa rozlaczne
            if node_low > j or node_high < i:
                return 0
            #case 2: Przedzial node_low-node_high zawiera sie w calosci w i-j
            if i <= node_low and node_high <= j:
                return self.heap[node]
            #case 2: przedzialy sie przecinaja
            mid = (node_low + node_high)//2
            sum_left_subtree = self._sum(left(node),node_low,mid,i,j)
            sum_right_subtree = self._sum(right(node),mid+1,node_high,i,j)
            return sum_left_subtree + sum_right_subtree

        def sum(self,i,j):
            #funkcja bedzie szukala ile jest liczb z przedzialu i-j
            #tak naprawde "i" w naszym przypadku zawsze bedzie wynosic 0
            #self.leaves - 1 to liczba lisci czyli prawdziwa tablica + zera (ktore nie maja wplywu na sume)
            return self._sum(0,0, self.leaves - 1,i,j)

    st = SegmentTree(k+1)
    n = len(T)
    coffee = 0
    for i in range(n-1,-1,-1):
        coffee += st.sum(0,T[i]-1)
        st.update(T[i])

    return coffee

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kawa, all_tests=True)
