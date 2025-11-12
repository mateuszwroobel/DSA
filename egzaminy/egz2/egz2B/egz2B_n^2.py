#Mateusz Wróbel
#Dla kazdego indeksu "i" przechodze w lewo i licze ile jest mniejszych od niej oraz takich, które nie zostały
#jeszcze usuniete. Jezeli napotykam taka liczbe to zmniejszam zmienna remain, ktora mowi ile liczb pozostanie.
#Do sprawdzenia czy juz usunalem liczbe uzywam tablicy deleted, ktora mowi czy juz usunalem dany indeks.
#Dodatkowo trzymam zmienna delete_own, która bedzie mi mowila czy nalezy usunac tez samego siebie.
#Na koniec zwracam liczbe pozostalych liczb
#Zlozonosc czasowa O(n^2)

from egz2Btesty import runtests


def bitgame(T):
    n = len(T)
    deleted = [False] * n
    remain = n

    for i in range(n):
        #zmienna do usuniecie indeksu "i"
        delete_own = False

        for j in range(i-1,-1,-1):
            if T[j] <= T[i] and not deleted[j]:
                delete_own = True #Bede musial usunac tez indeks i
                deleted[j] = True #Usuwam mniejsze liczby
                remain -= 1

            #Usuwanie indeksu i
            if delete_own and not deleted[i]:
                remain-= 1
                deleted[i] = True

    return remain

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
