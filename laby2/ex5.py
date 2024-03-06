"""
Zadanie 5. Podaj algorytm, który dla danego S > 0 sprawdza, czy w liście dodatkich liczb seq istnieje segment (spójny fragment listy) o sumie S. Inaczej, czy istnieja ̨indeksy i i j takie, z ̇e Pjk=i seq[k] = S?
"""

def find_segment_with_sum(S, seq):
    # Obliczenie sum prefiksowych
    prefix_sum = [0]
    for num in seq:
        prefix_sum.append(prefix_sum[-1] + num)

    # Wyszukiwanie binarne dla każdego elementu w sumach prefiksowych
    for i in range(len(seq)):
        target = S + prefix_sum[i] - seq[i]
        l, r = i + 1, len(prefix_sum) - 1
        while l <= r:
            mid = (l + r) // 2
            if prefix_sum[mid] == target:
                return True
            elif prefix_sum[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

    # Jeśli nie znaleziono żadnego odpowiedniego segmentu
    return False

import time


print('Małe testy...', end=' ')
beg = time.time()
# Test 1: Segment znajduje się na początku listy
assert find_segment_with_sum(3, [1, 2, 3, 4, 5]) == True
# Test 2: Segment znajduje się w środku listy
assert find_segment_with_sum(7, [1, 2, 3, 4, 5]) == True
# Test 3: Segment znajduje się na końcu listy
assert find_segment_with_sum(9, [1, 2, 3, 4, 5]) == True
# Test 4: Segment obejmuje całą listę
assert find_segment_with_sum(15, [1, 2, 3, 4, 5]) == True
# Test 5: Segment nie istnieje
assert find_segment_with_sum(16, [1, 2, 3, 4, 5]) == False
# Test 6: Pusta lista, segment nie istnieje
assert find_segment_with_sum(1, []) == False
end = time.time()
print(f'OK, czas: {end-beg:.3f}s')

# Większe testy
for i in range(2, 6):
    n = 10**i
    print(f'Lista długości {n}...', end=' ')
    beg = time.time()
    # Lista składająca się z samych jedyniek, segment o sumie 'n' na pewno istnieje
    assert find_segment_with_sum(n, [1]*n) == True
    # Lista składająca się z wartości rosnących od 1 do n, segment o sumie 'n' może nie istnieć
    assert find_segment_with_sum(n, list(range(1, n+1))) == False
    end = time.time()
    print(f'OK, czas: {end-beg:.3f}s')
    if end-beg > 1:
        print('Test zajął sporo czasu, pomijanie reszty testów')
        break
