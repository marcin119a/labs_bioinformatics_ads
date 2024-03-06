"""
Zadanie 2. Dana jest posortowana niemaleja ̨co lista A zawieraja ̨ca liczby całkowite. Znajdz ́ miejsce ostatniego wysta ̨pienia elementu x (lub zwróc ́ None gdy x nie wyste ̨puje w A).
"""
import time

#TODO SLOW

def rightmost_occurrence(x, A):
    l, r = 0, len(A) - 1
    result = None  # Zainicjalizuj wynik jako None, na wypadek gdyby x nie zostało znalezione

    while l <= r:
        mid = l + (r - l + 1) // 2  # Znajdź środkowy indeks

        # Sprawdź, czy środkowy element jest równy x
        if A[mid] == x:
            result = mid  # Zaktualizuj wynik bieżącym indeksem
            l = mid + 1  # Przesuń się w prawo, aby znaleźć pierwsze wystąpienie
        elif A[mid] < x:
            l = mid + 1  # Przesuń się w prawo, ponieważ x jest większe niż środkowy element
        else:
            r = mid - 1  # Przesuń się w lewo, ponieważ x jest mniejsze niż środkowy element

    return result


print('Test rightmost_occurrence()...', end=' ')
beg = time.time()
assert rightmost_occurrence(1, [1]) == 0
assert rightmost_occurrence(1, [1, 2]) == 0
assert rightmost_occurrence(2, [1, 2]) == 1
assert rightmost_occurrence(3, [1, 2, 2, 3, 3, 3, 4, 5, 6]) == 5
assert rightmost_occurrence(4, [1, 2, 2, 3, 3, 3, 4, 5, 6]) == 6
assert rightmost_occurrence(2, [1, 2, 2, 2, 3, 3, 4, 5]) == 3
assert rightmost_occurrence(5, [1, 2, 2, 2, 3, 3, 4, 5]) == 7
assert rightmost_occurrence(0, list(range(100000))) == 0
assert rightmost_occurrence(99999, list(range(100000))) == 99999
assert rightmost_occurrence(1, []) == None
assert rightmost_occurrence(6, [1, 2, 3, 4, 5]) == None
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')