"""
Zadanie 3. Dana jest posortowana niemaleja ̨co lista A zawierajaca liczby całkowite. Wyznacz liczbe ̨ wystąpien  elementu x w tablicy A.
"""
import time

from ex1 import leftmost_occurrence
from ex2 import rightmost_occurrence

def count_occurrences(x, A):
    if rightmost_occurrence(x, A) is None and rightmost_occurrence(x, A) is None:
        return 0
    if rightmost_occurrence(x, A) == leftmost_occurrence(x, A):
        return 1
    return rightmost_occurrence(x, A) - leftmost_occurrence(x, A) + 1


print('Test count_occurrence()...', end=' ')
beg = time.time()
assert count_occurrences(1, [1]) == 1
assert count_occurrences(2, [1]) == 0
assert count_occurrences(1, [1, 2]) == 1
assert count_occurrences(1, [1, 1]) == 2
assert count_occurrences(3, [1, 2]) == 0
assert count_occurrences(500, list(range(10000))) == 1
assert count_occurrences(3, [1, 2, 2, 3, 3, 3, 4, 5, 5, 5]) == 3
assert count_occurrences(10001, list(range(10000))) == 0
assert count_occurrences(1, [1] * 100000) == 100000
assert count_occurrences(1, []) == 0
assert count_occurrences(0, [1] * 100000) == 0
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')