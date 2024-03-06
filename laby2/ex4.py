"""
Mamy liste ̨ A o długości n dla której spełniona jest własnosć A[0] ≤ A[1] i A[n − 2] ≥ A[n − 1]. Element A[i] (dla 0 < i < n − 1) jest wierzchołkiem jes ́li A[i − 1] ≤ A[i] ≥ A[i + 1]. Zaproponuj algorytm znajduja ̨cy wierzchołek.
"""

import time


def find_peak(A):
    n = len(A)
    if n == 1 or A[0] >= A[1]:
        return 0  # Pierwszy element jest wierzchołkiem
    if A[n - 2] <= A[n - 1]:
        return n - 1  # Ostatni element jest wierzchołkiem

    for i in range(1, n - 1):
        if A[i - 1] <= A[i] and A[i] >= A[i + 1]:
            return i  # Znaleziono wierzchołek

def find_peak(A):
    l, r = 0, len(A) - 1

    while l < r:
        mid = (l + r) // 2
        # Sprawdź, czy jesteśmy na wierzchołku
        if A[mid] >= A[mid - 1] and A[mid] >= A[mid + 1]:
            return mid
        # W przeciwnym razie, idź w kierunku większego sąsiada
        elif A[mid] < A[mid - 1]:
            r = mid - 1
        else:
            l = mid + 1

    # Jeśli wyszliśmy z pętli, oznacza to, że 'l' jest wierzchołkiem
    return l




print('Małe testy...', end=' ')
beg = time.time()
assert find_peak([1, 2, 1]) in [1]  # Wierzchołek na pozycji 1
assert find_peak([1, 3, 2]) in [1]  # Wierzchołek na pozycji 1
assert find_peak([1, 2, 3, 4, 3]) in [3]  # Wierzchołek na pozycji 3
assert find_peak([1, 5, 3, 7, 3, 8, 4]) in [1, 3, 5]  # Wierzchołki na pozycjach 1, 3, 5
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')

# Większe testy
for i in range(2, 7):
    for j in (1, 2, 5):
        n = j * 10**i
        print(f'Lista długości {n}...', end=' ')
        beg = time.time()
        A = [i % 2 for i in range(n)]  # Lista z naprzemiennie 0 i 1, więc wierzchołki na każdej nieparzystej pozycji
        assert find_peak(A) % 2 == 1  # Sprawdzenie, czy znaleziono wierzchołek na nieparzystej pozycji
        end = time.time()
        print(f'OK, czas: {end-beg:.3f}s')
        if end-beg > 1:
            print('Test zajął sporo czasu, pomijanie reszty testów')
            break