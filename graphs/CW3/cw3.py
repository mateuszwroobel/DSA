'''
Zad1
Algorytm dijkstry rep macierzowa
'''
# def Dijkstra(G,s):
#     n = len(G)
#     visited = [False for _ in range(n)]
#     parent = [None for _ in range(n)]
#     d = [float('inf')for _ in range(n)]
#     d[s] = 0
#     q = priority.queue()
#     q.put((0,s))

'''
3.Najkrotsze sciezki w Dagu
    Dijkstry zadziala  chcemy cos szybszego
    Sortowanie topologiczne i algorytm Bellmana Forda

4.DLugoscia sciezki jest iloczyn jej wag. Zaproponowac jak najszybszy/najlepszy algorytm znajdujacy najkrotsze sciezki
    loga + logb = log(ab)
    i pozniej dijkstry(jezeli wagi beda powyzej 1) 
    lub belmman gdy wagi mniejsze od 1 
    
5.Przewodnik turystyczny
    Problem maksymalnej przepustowosci
    1. Umieszczamy w koeljsce priorytetowej wagi typu max
    2. Struktura union-find
    3. Iteracyjnie sciagamy z kolejki maksymalna krawedz
        u(max),v(max)
    4.Waga maksymalna jest pamietana i union find do tego momentu az S do T jest taki sam, wtedy to
    oznacza ze sa w jednym drzewie
    tworzymy maksymalne drzewo rozpinajace
     Jezeli z s do to wczesniej nie bylo krawedzi, a teraz maja wspolneg   o reprezentatna wiec sa juz polaczone i jako iz 
     idziemy po maksymalnej wadze to bezdie to maksymalna
     O(ElogV)
     Dijkstra
     ale bierzmy minimum w relaksacji zamiast sumy O(ElogV)
     Inne podejscie
     bfs lub dfs
    
6 Stazje benzynowe

7 Dwoch kierwocow
Jedziemy z s do t. Graf wazony. Kierwocy a i b. Bob decydyuje ktoredy beda jechac. Bob wybiera taka trase zeby
on prowadzil jak najmniej. Zamieniaja sie co stacje. Stacje to wierzcholki.
    W kolejce piorytetyowej przechowujemy pary kto wjechal, visited, distance musi byc na parach
    bo gdyby tylko dla kolejki by to nie zadzialalo
8 chcemy znalezc najkrotsza sciezke, przebiegajaca po malejacych wagach.

     
    
Zad 2.
Odtwarzanie/wypisywanie najkrotszej sciezki na podstawie 
tablicy parentow
'''
#zad2
def restore(parent,x): #x - wierzcholek docelowy
    path = [t]
    while parent[t] != None:
        path.append(parent[t])
        t=parent[t]
    return path
