"""
Zadanie 5. Podaj algorytm, który dla danego S > 0 sprawdza, czy w liście dodatkich liczb seq istnieje segment (spójny fragment listy) o sumie S. Inaczej, czy istnieja ̨indeksy i i j takie, z ̇e Pjk=i seq[k] = S?
"""

import time
SOL = 3
# O(n^2)

if SOL == 1:
    def find_segment_with_sum(S, seq):
        n = len(seq)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += seq[j]
                if current_sum == S:
                    return True
        return False

if SOL == 2:
    def find_segment_with_sum(S, seq):
        # Obliczenie sum prefiksowych
        prefix_sum = [0]
        for num in seq:
            prefix_sum.append(prefix_sum[-1] + num)

        # Wyszukiwanie binarne dla każdego elementu w sumach prefiksowych
        for i in range(1, len(prefix_sum)):  # Zaczynamy od 1, bo nie ma sensu szukać segmentu kończącego się przed pierwszym elementem
            l, r = 0, i - 1  # Zakres od 0 do i-1, bo szukamy segmentu kończącego się na prefix_sum[i] (włącznie)
            while l <= r:
                mid = (l + r) // 2
                if prefix_sum[i] - prefix_sum[mid] == S:
                    return True  # Znaleziono segment o sumie S
                elif prefix_sum[i] - prefix_sum[mid] < S:
                    r = mid - 1  # Suma jest za mała, szukaj w lewej połowie
                else:
                    l = mid + 1  # Suma jest za duża, szukaj w prawej połowie

        # Jeśli nie znaleziono żadnego odpowiedniego segmentu
        return False
    # O(n) algorytm gąsienicy
if SOL == 3:
    def find_segment_with_sum(S, seq):
        left, right, current_sum = 0, 0, 0

        while right < len(seq):
            if current_sum < S:
                current_sum += seq[right]
                right += 1
            elif current_sum == S:
                return True
            else:
                current_sum -= seq[left]
                left += 1

            # Sprawdzenie dla przypadku, gdy ostatni element jest równy S
            if current_sum == S:
                return True

        return False

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
    assert find_segment_with_sum(int((n+1)*n // 2), list(range(1, n+1))) == True

    assert find_segment_with_sum(int((n+1)*n // 2 + 1), list(range(1, n+1))) == False

    end = time.time()
    print(f'OK, czas: {end-beg:.3f}s')
    if end-beg > 1:
        print('Test zajął sporo czasu, pomijanie reszty testów')
        break