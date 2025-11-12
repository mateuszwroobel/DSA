#1. Tankowanie
'''
1
b. jadedo najblizszej tanszej stacji(mam na tyle paliwa)
nie ma tanszej stacji w obrebie L => tankuje na full na obecnej
n^2
nlogn - kopiec
c - j.w ale mmusimy tankowac do pelna

2. Zadania z terminamie
z1,z2,.......zn- zadania do wykonania (wykonanie kazdego trwa 1h)
d(zi) - po ilu godzinach zi powinno byc wykonane
g{zi} - zysk za wykonanie zi w czasie
Maksymalizacja zysku

3
Przyczepa o pojemnosci T
chcemy przyczepece zapelnic jak najbatdziej uzywajac
jak najmniej towaru

'''

#Tankowanie 1a S - pozycje stacji
def tank(S,L):
    n = len(S)
    cap = 0
    c = 0
    for i in range(1,n):
        cap -= S[i] - S[i-1]
        if cap < 0:
            cap += L
            c+=1
            if cap < 0:
                return False
    return c