"""
Zadanie 1. Dana jest posortowana niemaleja ̨co lista A zawieraja ̨ca liczby całkowite. Znajdz ́ miejsce (index) pierwszego wysta ̨pienia elementu x (lub zwróc ́ None gdy x nie wyste ̨puje w A).
"""
import time

#TODO SLOW

def leftmost_occurrence(x, A):
    l, r = 0, len(A) - 1
    result = None  # Zainicjalizuj wynik jako None, na wypadek gdyby x nie zostało znalezione

    while l <= r:
        mid = l + (r - l) // 2  # Znajdź środkowy indeks

        # Sprawdź, czy środkowy element jest równy x
        if A[mid] == x:
            result = mid  # Zaktualizuj wynik bieżącym indeksem
            r = mid - 1  # Przesuń się w lewo, aby znaleźć pierwsze wystąpienie
        elif A[mid] < x:
            l = mid + 1  # Przesuń się w prawo, ponieważ x jest większe niż środkowy element
        else:
            r = mid - 1  # Przesuń się w lewo, ponieważ x jest mniejsze niż środkowy element

    return result



# Testy
print('Test leftmost_occurrence()...', end=' ')
beg = time.time()
assert leftmost_occurrence(1, [1]) == 0
assert leftmost_occurrence(1, [1, 2]) == 0
assert leftmost_occurrence(2, [1, 2]) == 1
assert leftmost_occurrence(1, [1, 2, 2, 3, 3, 3, 4, 5, 6]) == 0
assert leftmost_occurrence(3, [1, 2, 2, 3, 3, 3, 4, 5, 6]) == 3
assert leftmost_occurrence(2, [1, 2, 2, 2, 3, 3, 4, 5]) == 1
assert leftmost_occurrence(4, [1, 2, 2, 2, 3, 3, 4, 5]) == 6
assert leftmost_occurrence(0, list(range(100000))) == 0
assert leftmost_occurrence(99999, list(range(100000))) == 99999
assert leftmost_occurrence(1, []) == None
assert leftmost_occurrence(6, [1, 2, 3, 4, 5]) == None
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')