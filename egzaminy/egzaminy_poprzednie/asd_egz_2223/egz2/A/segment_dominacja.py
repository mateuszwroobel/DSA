from egz2atesty import runtests

#Rozwiazanie wykorzystuje drzewo przedzialowe. Wiemy ze zakres liczb jest ograniczone dzieki, temu mozemu
#kazdy lisc traktowac jako licznik wartosci.
#Algorytm wykonuje nastepujace kroki:
#Sortuje pary po pierwszej wspolrzednej aby rozpatrywac tylko jedna wspolrzedna, poniewaz po prawej stronie od kazdej liczby beda liczby ktore
#napewno dominuja po maja wieksza pierwsza wspolrzedna lub rowna pierwsza i wieksza druga
#Pozostaje mi policzyc dla kazdego punktu ile jest liczb, ktore juz minalem i maja druga wspolrzedna takze
#mniejsza.
#Wykorzystuje do tego drzewo przedzialowe, ktore poda mi odpowiedz w czasie O(logn)
#Kazdy wezel w drzewie odpowiada za sume w przedziale i-j czyli tak naprawde ile jest liczb od i do j w dotychczasowo
#rozwazanych wspolrzednych "y"
#Podczas przegladania nalezy takze odejmowac, liczbe punktow, ktore maja takie same "x" bo zostana one
#niepotrzebnie zliczone
#np (2,5),(2,6),(2,7) dla (2,7) policzy ze dominujemy nad poprzednimi dwoma i odejmie 3 czyli nalezy jeszcze dodac 1


#Poprawka  - sortuje pierwsza rosnaco, druga malejaco aby nie odejmowac tych co maja te same "x"
#
def dominance(P):

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

    #sortuje po pierwszej wspolrzednej, jesli sa takie same to po drugiej
    P = sorted(P, key = lambda x: (x[0],-x[1]))
    n = len(P)
    st = SegmentTree(n+1)


    best = 0
    for i in range(n):
        x = P[i][0]
        y = P[i][1]
        dominating = st.sum(0,y-1)# +1 bo odejmuje tez sam siebie
        best = max(dominating,best)
        st.update(y)

    return best

runtests(dominance, all_tests=True)
