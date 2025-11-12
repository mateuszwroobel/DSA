#Rozwiazanie, bedzie uzywac drzewa przedzialowego
#Liscie beda koszykami na owoce,
#Kazdy wezel wewnetrzy bedzie trzymal maximum ze swoich dzieci
#Informuje nas to ile najwiecej owocow mozna jeszcze pomiescic w koszyku
#Szukajac odpowiedniego koszyka, bedziemy priorytetyzowac lewa czesc poddrzewa, aby byc zgodnym z warunkami zadania, czyli
#wkladac do koszyka po lewej stronie

def numOfUnplacedFruits(fruits, baskets):

    left = lambda i: 2*i+1
    right = lambda i: 2*i + 2
    parent = lambda i: (i-1)//2
    class SegmentTree():
        def __init__(self,n):
            self.leaves = 1
            while self.leaves < n:
                self.leaves*=2
            #drzewo binarne ma 2 * leaves - 1 wezlow

            self.heap = [0] * (2 * self.leaves - 1)
            #tutaj dodac mozna budowanie O(n)
            #dla wezlow wewntrzych max a dla lisci liczebnosc koszyka

        def update(self,i,val,build):
            #Parametry val - wartosc, ktora wstawiam do koszyka
            #k - odpowiednik koszyka jako lisc
            #i - orygianlny indeks w tablicy
            #liscie zaczynaja sie od indeksu self.leaves - 1
            k = self.leaves - 1 + i
            if build:
                self.heap[k] = val
            #gdy wsadzimy jedne owoce nie mozemy juz drugich
            else:
                self.heap[k] = 0
            while k > 0:
                k = parent(k)
                self.heap[k] = max(self.heap[left(k)], self.heap[right(k)])

        def find_basket(self,fruits):
            k = 0
            if self.heap[0] < fruits:
                #nie bedzie miejsca dla owoca w kopcu
                return False

            #chce aby ostatnie wywolanie "k" dalo nam liscia, gdzie nalezy wsadzic
            while  k < self.leaves -1:
                if self.heap[left(k)] >= fruits:
                    #priorytet w lewo
                    k = left(k)
                else:
                    k = right(k)

            return k - (self.leaves-1) #da nam oryginalny indeks

    n = len(baskets)
    st = SegmentTree(n)

    #budowane drzewa w O(nlogn)
    for i in range(n):
        st.update(i,baskets[i],True)

    cant_put = 0
    for i in range(n):
        where = st.find_basket(fruits[i])
        if where is False:
            cant_put +=1
        else:
            st.update(where,0,False)

    return cant_put

fruits = [4,2,5]
baskets =[3,5,4]
print(numOfUnplacedFruits(fruits,baskets))








