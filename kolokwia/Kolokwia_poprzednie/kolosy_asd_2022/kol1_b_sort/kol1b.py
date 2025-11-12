
from kol1btesty import runtests

def f(T):

    return

def string_to_list(string):
    lista = [0 for _ in range(26)]
    for char  in string:
        lista[ord(char)-97]+=1  #dzieki temu otrzymam liczby z zakresu [0,25]
    return lista


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
#runtests( f, all_tests=True )
