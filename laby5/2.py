from typing import List


def subset_sum(arr, k):
    # Inicjowanie tablicy programowania dynamicznego
    n = len(arr)

    dp = [[False for j in range(k + 1)] for i in range(n + 1)]
    # Ustawianie dp[0][0] na True
    dp[0][0] = True

    # Wypełnianie tablicy dp
    for i in range(1, n + 1):
        dp[i][0] = True
        for j in range(1, k + 1):
            # Jeśli poprzednia suma jest True, obecna również musi być, właczamy element
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else: #bez tego elementu 
                # Sprawdzenie, czy suma jest możliwa z obecnym lub bez niego
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    # Ostateczny wynik
    return dp[n][k]


def subset_sum(arr: List[int], k: int) -> bool:
    possible = [1] + [0]*k
    for x in arr:
        for i in range(k+1-x)[::-1]:    # Przechodzimy od końca ([::-1] odwraca kolejność) wszystkie elementy od k-x (włącznie) do 0.
            if possible[i]: possible[i+x] = 1
    return possible[k] == 1

assert subset_sum([], 0) == True
assert subset_sum([], 3) == False

assert subset_sum([1, 2, 3, 4], 0) == True
assert subset_sum([1, 2, 3, 4], 6) == True
assert subset_sum([1, 2, 3, 4], 11) == False

assert subset_sum([2, 2, 4, 6], 5) == False

assert subset_sum([2, 2, 10, 20], 4) == True
assert subset_sum([2, 2, 10, 20], 22) == True
assert subset_sum([2, 2, 10, 20], 16) == False

assert subset_sum([1, 2, 4, 8, 16, 32, 64], 55) == True
assert subset_sum([1, 2, 4, 8, 16, 32, 64], 71) == True
assert subset_sum([1, 2, 4, 8, 16, 32, 64], 99) == True

assert subset_sum([1, 4, 8, 16, 32, 64], 55) == False
assert subset_sum([1, 4, 8, 16, 32, 64], 71) == False
assert subset_sum([1, 4, 8, 16, 32, 64], 99) == False
assert subset_sum([1, 4, 8, 16, 32, 64], 100) == True

print('Wszystkie testy zaliczone!')
