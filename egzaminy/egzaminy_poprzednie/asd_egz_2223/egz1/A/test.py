import heapq
from egz1Atesty import runtests
import math

def gold(G, V, s, t, r):
    """
    Znajduje trasę o najmniejszym koszcie (lub największym zysku) dla Złycerza
    przy użyciu rozszerzonego grafu stanów (wierzchołek, status_rabunku).

    Args:
        G: Graf w postaci listy sąsiedztwa. G[u] zawiera listę krotek (v, w),
           gdzie v to sąsiad u, a w to waga krawędzi u -> v. Zakładamy, że
           jeśli krawędź (u, v) istnieje z wagą w, to (v, u) również istnieje
           z tą samą wagą (graf nieskierowany reprezentowany jako skierowany).
           (Na podstawie przykładu)
        V: Lista zawierająca liczbę sztabek złota w każdym zamku (wierzchołku).
        s: Wierzchołek początkowy.
        t: Wierzchołek końcowy.
        r: Wysokość łapówki płaconej po obrabowaniu zamku.

    Returns:
        Najmniejszy koszt trasy. Ujemna wartość oznacza zysk.
        Zwraca math.inf jeśli t jest nieosiągalne.
    """
    n = len(G)
    # dist[u][0] - minimalny koszt dotarcia do wierzchołka u bez rabowania
    # dist[u][1] - minimalny koszt dotarcia do wierzchołka u po obrabowaniu jednego zamku
    dist = [[float('inf')] * 2 for _ in range(n)]

    # Kolejka priorytetowa: (koszt, wierzchołek, status_rabunku)
    # status_rabunku: 0 - nie obrabowany, 1 - obrabowany
    pq = []

    # Startujemy w wierzchołku s, nieobrabowani, z kosztem 0
    dist[s][0] = 0
    heapq.heappush(pq, (0, s, 0))

    while pq:
        cost, u, robbed_status = heapq.heappop(pq)

        # Jeśli znaleźliśmy już lepszą ścieżkę do tego stanu, pomijamy
        # Używamy <= bo Dijkstra może dodać stan z tym samym kosztem, a my chcemy go przetworzyć
        if cost > dist[u][robbed_status]:
             continue

        # Możliwość rabunku w obecnym wierzchołku u (tylko jeśli nie obrabowaliśmy wcześniej)
        if robbed_status == 0:
            # Nowy koszt po rabunku = obecny koszt - zysk (V[u])
            robbery_cost = cost - V[u]

            # Jeśli obrabowanie zamku u i przejście w stan 'obrabowany' jest lepsze
            # niż dotychczasowy minimalny koszt do stanu (u, 1)
            if robbery_cost < dist[u][1]:
                dist[u][1] = robbery_cost
                heapq.heappush(pq, (dist[u][1], u, 1))

        # Przejście do sąsiadów
        for v, weight in G[u]:
            # Koszt krawędzi zależy od statusu rabunku
            edge_cost = weight if robbed_status == 0 else 2 * weight + r
            new_cost = cost + edge_cost

            # Jeśli znaleziona ścieżka do v w tym samym statusie rabunku jest lepsza
            if new_cost < dist[v][robbed_status]:
                dist[v][robbed_status] = new_cost
                heapq.heappush(pq, (dist[v][robbed_status], v, robbed_status))

    # Najmniejszy koszt dotarcia do wierzchołka t to minimum z kosztów
    # dotarcia w stanie nieobrabowanym i w stanie obrabowanym.
    min_cost_to_t = min(dist[t][0], dist[t][1])

    # Jeśli minimalny koszt to nadal nieskończoność, t jest nieosiągalne
    return min_cost_to_t
runtests(gold, all_tests=True)