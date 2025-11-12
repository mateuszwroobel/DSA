from egzP5atesty import runtests 


#Do rozwiazania potrzebuje znalezc wczesniesszy mniejszy element, i pozniejszy mniejszy element
#wczesniejszy mniejsze element - pierwszy element po lewej stronie, ktory jest mniejsze od aktualnego
#pozniejszy mniejszy element - pierwszy element po prawej stronie ktory jest mniejszy od akutalnego
#Do rozwiazania bede uzywal stosu, ktory bedzie monotoniczny
#Bedzie to stos ktorego wartosci elemementow beda coraz mniejsze idac w dol
#Przechodze po po tablicy dwa razy: od lewej i od prawej i znajduje rozwiazanie
#Znajdowanie odbywa sie nastepujaco (od lewej):
#Przechodze po tablicy utrzymujac monotonicznosc stosu, element ktory jest u gory to nastepny mniejszy element
#Jesli stos jest pusty oznacza ze nie ma mniejszego elementu po lewej
#Teraz Mozna to wykorzystac do znalezienia sumy dzialek
#Dla kazdego indeksu suma bedzie wynosic:
#se[i] - pse[i]  - 1
def inwestor ( T ):
    n = len(T)
    #pse - previous smaller element, nse - next smaller element
    stack_pse = []
    pse = [-1] * n #jesli po lewej nie ma mniejszego to moge budowac od poczatku
    stack_nse = []
    nse = [n] * n #analogicznie jak pse
    for i in range(n):

        while stack_pse and stack_pse[-1][0] >= T[i]:
            stack_pse.pop()

        if stack_pse:
            pse[i] = stack_pse[-1][1]

        stack_pse.append((T[i],i))

    for i in range(n-1,-1,-1):

        while stack_nse and stack_nse[-1][0] >= T[i]:
            stack_nse.pop()

        if stack_nse:
            nse[i] = stack_nse[-1][1]

        stack_nse.append((T[i],i))

    best = 0

    for i in range(n):
        len_of_fragment = nse[i] - pse[i] - 1
        sum_of_field =  T[i] * len_of_fragment
        best = max(best,sum_of_field)


    return best

runtests ( inwestor, all_tests=True )