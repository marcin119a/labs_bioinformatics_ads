import time, sys
# TODO: przerobić wspólnie kilka algorytmów.

def max_subsequence(seq):
    # seq jest listą liczb całkowitych (dodatnich i ujemnych).
    # TODO: funkcja powinna znajdować spójny fragment listy "seq" o maksymalnej sumie.
    return 0


# Testy
print('Małe testy...', end=' ')
beg = time.time()
assert max_subsequence([2, -1, 3]) == 4
assert max_subsequence([1, 2, 3]) == 6
assert max_subsequence([-1, 2, 3, 4, -1]) == 9
assert max_subsequence([5, -6, 3, -5, 100, -1, 4, -1, 3, -4]) == 105
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')

for i in range(2, 7):
    for j in (1, 2, 5):
        n = j * 10**i
        print(f'Lista długości {n}...', end=' ')
        beg = time.time()
        assert max_subsequence([2, -1]*(n//2)) == n//2+1
        end = time.time()
        print(f'OK, czas: {end-beg:.3f}s')
        if end-beg > 1:
            print('Test zajął sporo czasu, pomijanie reszty testów')
            sys.exit()