import heapq
from typing import List, Tuple

"""
musimy zastosować priorytetową kolejkę do wyboru wierzchołka o najmniejszym obecnie znanym koszcie. 
Wersja algorytmu Dijkstry, która działa w czasie O(mlogm), używa stosu binarnego do przechowywania wierzchołków do przetworzenia
"""

# Przykład korzystania z biblioteki "heapq".
# Uwaga - nie mamy operacji "Decrease"!
def heapq_example():
    heap = []   # Tworzymy pusty kopiec (zwykła pusta lista).
    heapq.heappush(heap, 5) # Dorzucamy do niego element (liczbę 5).
    heapq.heappush(heap, 7) # Dorzucamy 7.
    heapq.heappush(heap, 3) # Dorzucamy 3.
    print(heapq.heappop(heap))  # Wyrzucamy najmniejszy(!) element z kopca - 3.
    heapq.heappush(heap, 10) # Dorzucamy 10.
    print(heapq.heappop(heap))  # Wyrzucamy najmniejszy(!) element z kopca - 5.



def dijkstra(n: int, v: List[List[Tuple[int, int]]]) -> int:
    # Wierzchołki mają numery od 0 do n-1.
    # v[x] - lista par (wierzchołek, długość/waga/koszt krawędzi).
    # np. v[1] = [(3, 100), (5, 200)] oznacza, że z wierzchołka 1 wychodzą dwie krawędzie:
    # do wierzchołka 3 o koszcie 100 i do wierzchołka 5 o koszcie 200.

    # Funkcja powinna zwracać minimalny koszt ścieżki z wierzchołka 0 do wierzchołka n-1.
    # (można założyć, że istnieje przynajmniej jedna taka ścieżka)

    # Priorytetowa kolejka do przechowywania wierzchołków do przetworzenia
    priority_queue = [(0, 0)]  # (distance, node)
    # Tablica odległości
    distances = [float('inf')] * n
    distances[0] = 0
    # Zbiór odwiedzonych wierzchołków
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in v[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[n-1]

# Testy.

assert dijkstra(2, [[(1, 100)], []]) == 100
assert dijkstra(2, [[(1, 100)], [(0, 10)]]) == 100

assert dijkstra(3, [[(1, 10), (2, 100)], [(2, 20)], []]) == 30

assert dijkstra(4, [[(1, 10), (2, 10), (3, 10)], [(0, 10), (2, 10), (3, 10)], [(0, 10), (1, 10), (3, 10)], [(0, 10), (1, 10), (2, 10)]]) == 10

assert dijkstra(7, [
    [(1, 2), (2, 8), (3, 3), (5, 2)],
    [(2, 5)],
    [],
    [(2, 5), (4, 1), (6, 3)],
    [(6, 1)],
    [(4, 3)],
    [(2, 1)]
]) == 5
