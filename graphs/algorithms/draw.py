import matplotlib.pyplot as plt
import networkx as nx

# Definicja listy sąsiedztwa
adjacency_list = [[(1, 633), (2, 849), (3, 1218), (4, 2550)], [(0, 633), (4, 362)], [(0, 849), (3, 21), (4, 3044)], [(0, 1218), (2, 21)], [(0, 2550), (1, 362), (2, 3044)]]

# Tworzymy pusty graf
G = nx.Graph()

# Dodajemy wierzchołki i krawędzie do grafu
for node, neighbors in enumerate(adjacency_list):
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Rysowanie grafu
pos = nx.spring_layout(G)  # Określamy sposób rozmieszczenia wierzchołków
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')

# Rysujemy wagi krawędzi
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Wyświetlamy graf
plt.title("Graf z listy sąsiedztwa")
plt.show()
