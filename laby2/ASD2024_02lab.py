import time, sys

def leftmost_occurrence(x, A):
    # A jest posortowaną niemalejąco listą liczb całkowitych, x jest liczbą całkowitą.
    # TODO: funkcja powinna znajdować pierwsze miejsce (indeks) wystąpienia elementu x w liście A.
    return None

def rightmost_occurrence(x, A):
    # A jest posortowaną niemalejąco listą liczb całkowitych, x jest liczbą całkowitą.
    # TODO: funkcja powinna znajdować ostanie miejsce (indeks) wystąpienia elementu x w liście A.
    return None

def count_occurrences(x, A):
    # A jest posortowaną niemalejąco listą liczb całkowitych, x jest liczbą całkowitą.
    # TODO: funkcja powinna znajdować liczbę wystąpień elementu x w liście A.
    return 0


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
nd = time.time()
print(f'OK, czas: {end-beg:.3f}s')