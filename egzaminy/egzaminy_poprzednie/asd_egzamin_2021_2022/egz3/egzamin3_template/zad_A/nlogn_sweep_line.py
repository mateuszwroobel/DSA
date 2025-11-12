from egz3atesty import runtests
#(Onlogn)
#Kazdy przedzial (a,b) traktuje jako dwie nowe operacje
#(a,+1)
#(b+1,-1)
#Posortuje wszystkie wartosci z tablicy i bede szedl od lewej, dla kazdego poczatku przedzialu bede dodawac 1
#co odpowiada ze zaczyna tam padac snieg, a gdy napotkam koniec przedzialu to odejmuje 1
#np przedzial (2,4)
#(2,+1), (4+1,-1) - dodam 1 dla 2,3,4, i od 5 odejme jeden co odpowiada ze tam nie pada juz snieg
def snow(T, I):
    n = len(I)
    A = []
    for x,y in I:
        A.append((x,+1))
        A.append((y+1,-1)) #potrzebne aby policztylo przedzial od a do b lacznie
    A = sorted(A, key = lambda x: (x[0],x[1])) #zawyza bez sortowania po drugiej
    curr = 0
    best = 0

    for v, operation in A:
        curr+=operation
        best = max(curr,best)
    return best

# uruchom testy
runtests(snow, all_tests=True)