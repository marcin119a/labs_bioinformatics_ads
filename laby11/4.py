import heapq
from typing import List, Tuple

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
    return 0


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
