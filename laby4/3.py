from typing import List, Optional


def subset_sum(arr, k):
    n = len(arr)
    dp = [[False for j in range(k + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    if not dp[n][k]:
        return None  # Zwraca None, jeśli nie ma takiego podzbioru

    # Wsteczne śledzenie, aby znaleźć elementy podzbioru
    subset = []
    i, j = n, k
    while j > 0 and i > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(arr[i - 1])
            j -= arr[i - 1]
        i -= 1

    return subset


# Testowanie.

# Funkcja sprawdza, czy lista *a* jest podciągiem listy *b*.
def subsequence(a: List[int], b: List[int]) -> bool:
    i = 0
    for x in b:
        if i < len(a) and x == a[i]: i += 1
    return i == len(a)

count = 0
def test(arr: List[int], k: int, solution_exists: bool = True):
    global count
    count += 1
    print(f'Test {count}...', end=' ')
    subset = subset_sum(arr, k)
    debug = f'arr: {arr}, k: {k}, zwrócony zbiór: {subset}'
    if subset is None:
        if solution_exists: raise RuntimeError(f'Zwrócono None, a istnieje rozwiązanie! {debug}')
    else:
        if sum(subset) != k: raise RuntimeError(f'Zbiór nie sumuje się do k! {debug}')
        if not subsequence(sorted(subset), sorted(arr)): raise RuntimeError(f'Nie zwrócono liczb z listy!\n{debug}')
    print('OK!')


test([], 0)
test([], 3, solution_exists=False)

test([1, 2, 3, 4], 0)
test([1, 2, 3, 4], 6)
test([1, 2, 3, 4], 11, solution_exists=False)

test([2, 2, 4, 6], 5, solution_exists=False)

test([2, 2, 10, 20], 4)
test([2, 2, 10, 20], 22)
test([2, 2, 10, 20], 16, solution_exists=False)

test([1, 2, 4, 8, 16, 32, 64], 55)
test([1, 2, 4, 8, 16, 32, 64], 71)
test([1, 2, 4, 8, 16, 32, 64], 99)

test([1, 4, 8, 16, 32, 64], 55, solution_exists=False)
test([1, 4, 8, 16, 32, 64], 71, solution_exists=False)
test([1, 4, 8, 16, 32, 64], 99, solution_exists=False)
test([1, 4, 8, 16, 32, 64], 100)

print('Wszystkie testy zaliczone!')
