from kol1testy import runtests

#Sortuje malejaco - element, którego roznica indeksow miedzy pierwotna a posortowana jest najwieksza to max rank.
#Jezeli element zmienil pozyzje o "k" oznacza to ze przed nim bylo "k" mniejszych liczb bo teraz przeskoczyl w lewo te liczby mniejsze od siebie
#Elementy ktore byly po prawej stronie od rozpatrywnego nadal beda poprawej, wiec nie wplywaja na range
#Wazne jest aby posortowac stabilnie.
def maxrank(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i],i)
    T = sorted(T,key=lambda x: (-x[0],x[1]))
    best = 0
    for current_index,element in enumerate(T):
        prev_index = element[1]
        diff = prev_index - current_index
        best = max(best,diff)
    return best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=True)
