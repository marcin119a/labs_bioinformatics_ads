def max_subsequence(seq):
    max_sum = 0  # Największa znaleziona suma
    current_sum = 0  # Suma bieżącego podciągu

    for element in seq:
        current_sum += element  # Dodaj bieżący element do sumy bieżącego podciągu
        if current_sum < 0:
            current_sum = 0  # Jeśli suma bieżącego podciągu jest ujemna, resetuj ją
        max_sum = max(
            max_sum, current_sum)  # Aktualizuj maksymalną sumę, jeśli to konieczne

    return max_sum


# rozwiązanie (n^3)
def max_subsequence(seq):
    n = len(seq)
    max_sum = 0  # Zakładamy, że maksymalna suma podciągu nie może być mniejsza niż 0

    for start in range(n):  # Punkt początkowy podciągu
        for end in range(start, n):  # Punkt końcowy podciągu
            current_sum = 0
            for i in range(start, end + 1):  # Obliczenie sumy podciągu
                current_sum += seq[i]
            max_sum = max(max_sum, current_sum)  # Aktualizacja maksymalnej sumy

    return max_sum


# rozwiazanie (n^2)
def max_subsequence2(seq):
    n = len(seq)
    max_sum = 0  # Zakładamy, że maksymalna suma podciągu nie może być mniejsza niż 0
    prefix_sums = [0]

    # Obliczanie sum prefiksowych
    for i in range(n):
        prefix_sums.append(prefix_sums[-1] + seq[i])

    # Wyszukiwanie maksymalnej sumy podciągu
    for start in range(n):
        for end in range(start, n):
            # Suma podciągu od start do end = suma prefiksowa do end - suma prefiksowa przed start
            current_sum = prefix_sums[end + 1] - prefix_sums[start]
            max_sum = max(max_sum, current_sum)

    return max_sum


import time, sys



# Testy
print('Małe testy...', end=' ')
beg = time.time()
assert max_subsequence([2, -1, 3]) == 4
assert max_subsequence([1, 2, 3]) == 6
assert max_subsequence([-1, 2, 3, 4, -1]) == 9
assert max_subsequence([5, -6, 3, -5, 100, -1, 4, -1, 3, -4]) == 105
end = time.time()
print(f'OK, czas: {end - beg:.3f}s')

for i in range(2, 7):
    for j in (1, 2, 5):
        n = j * 10 ** i
        print(f'Lista długości {n}...', end=' ')
        beg = time.time()
        assert max_subsequence([2, -1] * (n // 2)) == n // 2 + 1
        end = time.time()
        print(f'OK, czas: {end - beg:.3f}s')
        if end - beg > 2:
            print('Test zajął sporo czasu, pomijanie reszty testów')
            sys.exit()