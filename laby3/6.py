from typing import List, Optional

def height(parent: List[Optional[int]]):
    # TODO: uzupełnij tę funkcję.
    # Wierzchołkami w drzewie są liczby od 0 do len(parents)-1.
    # Wartość parent[x] oznacza rodzica wierzchołka x (jeśli jest równa None, to znaczy, że x jest korzeniem drzewa).
    # Funkcja powinna zwrócić wysokość drzewa (długość najdłuższej ścieżki z korzenia do liścia).
    return 0


# Testowanie.

assert height([None]) == 0, "Jeden wierzchołek"
assert height([None, 0]) == 1, "Dwa wierzchołki, 0 jest korzeniem"
assert height([1, None]) == 1, "Dwa wierzchołki, 1 jest korzeniem"
assert height([None, 0, 0, 0, 0]) == 1, "Gwiazda (wszyscy są dziećmi korzenia)"
assert height([None, 0, 1, 2, 3, 4, 5]) == 6, "Ścieżka długości 5"
assert height([None, 0, 1, 2, 3, 0, 5, 6, 7]) == 4, "Dwie ścieżki wychodzące z korzenia"
assert height([1, 3, 4, 2, None]) == 4, "Ścieżka, ale z pomieszanymi numerami"

assert height([None, 0, 0, 1, 0, 3, 3, 3, 6, 3, 1]) == 4, "Losowe drzewo o 10 wierzchołkach, rodzic ma zawsze niższy numer niż dziecko"
assert height([3, 2, None, 9, 9, 2, 9, 9, 2, 5]) == 4, "Losowe drzewo o 10 wierzchołkach (to samo co powyżej, tylko z pomieszanymi numerami)"

assert height([None, 0, 0, 1, 0, 3, 3, 3, 6, 3, 1, 7, 0, 6, 6, 9, 0, 14, 8, 7, 18, 3, 10, 0, 0, 0, 20, 17, 0, 28, 12, 21, 13, 27, 1, 33, 14, 28, 31, 35, 14, 22, 14, 14, 29, 18, 1, 26, 35, 41, 6, 11, 40, 46, 18, 7, 47, 21, 57, 46, 45, 32, 59, 61, 54, 64, 24, 38, 36, 63, 64, 50, 4, 61, 31, 51, 53, 22, 46, 70, 47, 11, 56, 65, 13, 20, 66, 50, 47, 62, 3, 60, 5, 39, 90, 78, 75, 74, 50, 82, 21]) == 11, "Losowe drzewo o 100 wierzchołkach, rodzic ma zawsze niższy numer niż dziecko"
assert height([24, 26, 47, 94, 75, 10, 19, 85, 30, 6, 13, 4, 23, 55, 24, 88, 80, 47, 19, None, 33, 77, 20, 19, 57, 16, 14, 19, 22, 54, 10, 19, 33, 23, 30, 15, 23, 8, 10, 80, 55, 55, 86, 19, 81, 40, 40, 55, 42, 37, 59, 72, 28, 38, 22, 33, 19, 33, 62, 20, 19, 31, 27, 47, 40, 33, 75, 57, 15, 65, 68, 96, 5, 37, 63, 12, 41, 99, 47, 47, 23, 39, 86, 53, 41, 76, 19, 53, 74, 85, 83, 79, 57, 87, 33, 89, 80, 32, 17, 37]) == 11, "Losowe drzewo o 100 wierzchołkach (to samo co powyżej, tylko z pomieszanymi numerami)"
