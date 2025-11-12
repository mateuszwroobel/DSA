# O(n^2) bruteforce
def reconstructQueue_nsquare(self, people):
    # Algorytm bedzie wykonaywal nastepujace kroki
    # Biore z tablicy taka pare ze druga wartosc to 0, a pierwsza jest minimalna:
    # Pozniej przechodze po tablicy i zmniejszam o 1 druga krotke tych, ktora maja wzrost mniejszy
    # badz rowny, dlatego ze juz zabralem jeden element wiec nalezy go odjac
    # Te kroki nalezy powtarzac, az dodam do kolejki wszystkie elementy
    # Mozna ulepszyc sortuajc po wzroscie
    n = len(people)
    ans = []
    # pomoc
    people = sorted(people, key=lambda x: x[0])
    orginal = [[x, y] for x, y in people]
    mini = max(people)
    i = 0
    j = 0
    while len(ans) < n:
        # szukanie elementu
        for i in range(n):
            value = people[i][0]
            k = people[i][1]
            if k == 0 and mini > value:
                mini = value
                to_pop = orginal[i]

        ans.append(to_pop)

        # zmniejszanie o 1 drugiej wartosci
        for i in range(n):
            value = people[i][0]
            # mozna zakonczyc wczesniej bo sa posortowane
            if value > mini:
                break
            if value <= mini:
                people[i][1] -= 1
        mini = max(people)
    return ans







