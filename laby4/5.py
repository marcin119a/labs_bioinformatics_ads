class DisjointSet:
    def __init__(self, n):
        # Każdy wierzchołek w swoim własnym zbiorze
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # Używane do optymalizacji

    def find(self, u):
        # Znajdowanie reprezentanta zbioru (korzenia)
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Ścieżka kompresji
        return self.parent[u]

    def union(self, u, v):
        # Łączenie dwóch zbiorów
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
"""
https://visualgo.net/en/mst
Klasa DisjointSet:
Inicjalizacja: Każdy wierzchołek grafu znajduje się w swoim własnym zbiorze.
Find: Metoda znajduje reprezentanta zbioru, do którego należy dany wierzchołek.
Union: Metoda łączy dwa zbiory (zbiory, do których należą dwa różne wierzchołki) w jeden.
Algorytm Kruskala:
Sortowanie krawędzi: Krawędzie są sortowane rosnąco według wagi.
Iteracja po krawędziach: Dla każdej krawędzi w posortowanej liście sprawdzamy, czy jej wierzchołki należą do różnych zbiorów (co oznacza, że dodanie krawędzi nie spowoduje powstania cyklu).
Budowanie drzewa: Jeśli wierzchołki należą do różnych zbiorów, dodajemy krawędź do wynikowego drzewa i łączymy zbiory.
"""
def kruskal(n, edges):
    # Inicjalizacja struktury zbiorów rozłącznych
    dsu = DisjointSet(n)
    mst = []  # Minimalne drzewo rozpinające
    total_weight = 0  # Łączna waga drzewa

    # Sortowanie krawędzi po wagach
    edges.sort(key=lambda x: x[2])

    # Iteracja po posortowanych krawędziach
    for u, v, weight in edges:
        # Sprawdzenie, czy u i v należą do różnych zbiorów
        if dsu.find(u) != dsu.find(v):
            # Dodanie krawędzi do drzewa
            mst.append((u, v, weight))
            total_weight += weight
            # Łączenie zbiorów
            dsu.union(u, v)

    return mst, total_weight

n = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

# Wywołanie algorytmu Kruskala
kruskal_result = kruskal(n, edges)
kruskal_result