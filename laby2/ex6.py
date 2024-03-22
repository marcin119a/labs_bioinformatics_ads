"""
Zadanie 6. Mamy dana ̨ liczbe ̨ całkowita ̨ k (1 ≤ k ≤ 106) oraz dwie listy A i B, o długości m i n, zawierajace liczby naturalne nie większe niż k.
Napisz algorytm sprawdzaja ̨cy czy można zamienić po jednym elemencie list A i B tak aby po zamianie sumy elementów tych list były równe.
"""

#O(n+m)
def can_swap_to_equal_sum(A, B):
    sumA, sumB = sum(A), sum(B)
    diff = sumA - sumB

    # Jeśli różnica jest nieparzysta, zamiana nie jest możliwa
    if diff % 2 != 0:
        return False

    target = diff // 2
    B_set = set(B)

    for a in A:
        if (a - target) in B_set:
            return True  # Znaleziono parę elementów do zamiany

    return False  # Nie znaleziono odpowiedniej pary elementów

# Przykładowe użycie
assert can_swap_to_equal_sum([1, 2, 3], [4, 5, 6]) == False

import time
for i in range(2, 6):
    n = 10**i
    print(f'Lista długości {n}...', end=' ')
    beg = time.time()

    # Listy, gdzie zamiana jest możliwa: różnica sum wynosi 2, a istnieje para elementów, których zamiana wyrównuje sumy
    A = [1] * n
    B = [3] + [1] * (n - 1)
    assert can_swap_to_equal_sum(A, B) == True

    # Listy, gdzie zamiana jest niemożliwa: różnica sum jest parzysta, ale nie ma pary elementów do zamiany
    A = [2] * n
    B = [4] * n
    assert can_swap_to_equal_sum(A, B) == False

    # Listy, gdzie zamiana jest możliwa: różnica sum wynosi 0, więc listy już mają równe sumy
    A = [5] * n
    B = [5] * n
    assert can_swap_to_equal_sum(A, B) == True

    end = time.time()
    print(f'OK, czas: {end-beg:.3f}s')
    if end-beg > 1:
        print('Test zajął sporo czasu, pomijanie reszty testów')
        break

