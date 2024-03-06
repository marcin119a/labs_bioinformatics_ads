import time
import sys

def is_subsequence(A, B):
    i, j = 0, 0  # Indeksy dla A i B

    while i < len(A) and j < len(B):
        if A[i] == B[j]:  # Znaleziono pasujący element
            i += 1  # Przesuń indeks w A
        j += 1  # Przesuń indeks w B

    return i == len(A)  # Czy przeszliśmy przez całą tablicę A?

print('Małe testy...', end=' ')
beg = time.time()
assert is_subsequence([1, 3], [1, 2, 3, 4]) == True
assert is_subsequence([1, 5], [1, 2, 3, 4]) == False
assert is_subsequence([1, 2, 3], [1, 2, 3]) == True
assert is_subsequence([], [1, 2, 3]) == True  # Pusta lista jest podciągiem każdej listy
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')

for i in range(2, 7):
    for j in (1, 2, 5):
        n = j * 10**i
        m = 2 * n
        A = [x % 5 for x in range(n)]  # A będzie miała elementy od 0 do 4
        B = A + [5] * n  # B zawiera A, więc A musi być podciągiem B
        print(f'Lista A długości {n} i lista B długości {m}...', end=' ')
        beg = time.time()
        assert is_subsequence(A, B) == True
        end = time.time()
        print(f'OK, czas: {end-beg:.3f}s')
        if end - beg > 2:
            print('Test zajął sporo czasu, pomijanie reszty testów')
            sys.exit()