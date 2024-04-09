from typing import List, Sequence

#O(n log(n) + n^2)
def three_numbers_of_small_sum(nums: List[int], k: int) -> Sequence[int]:
    nums.sort()

    # Dla każdej liczby w liście jako potencjalny pierwszy kandydat
    for i in range(len(nums) - 2):
        # Inicjowanie wskaźników dla pozostałych dwóch liczb
        left, right = i + 1, len(nums) - 1

        while left < right:
            # Obliczanie sumy trzech liczb
            current_sum = nums[i] + nums[left] + nums[right]

            # Jeśli suma jest mniejsza lub równa k, zwracamy te liczby
            if current_sum <= k:
                return (nums[i], nums[left], nums[right])

            # Jeśli suma jest większa niż k, przesuwamy wskaźnik 'right' w lewo
            elif current_sum > k:
                right -= 1

            # Jeśli suma jest mniejsza, to zwiększamy sumę przesuwając 'left'
            else:
                left += 1

    # Jeśli nie znajdziemy żadnych trzech liczb, zwracamy None
    return None

# Testowanie.
#O(nlog(n))
def three_numbers_of_small_sum(arr: List[int], k: int) -> Sequence[int]:
    return sorted(arr)[:3]


# Funkcja sprawdza, czy lista *a* jest podciągiem listy *b*.
def subsequence(a: List[int], b: List[int]) -> bool:
    i = 0
    for x in b:
        if i < len(a) and x == a[i]: i += 1
    return i == len(a)

count = 0
def test(arr: List[int], k: int):
    global count
    count += 1
    print(f'Test {count}...', end=' ')
    answer = three_numbers_of_small_sum(arr[:], k)
    debug = f'lista: {arr}, k: {k}, zwrócona wartość: {answer}'
    if len(answer) != 3: raise RuntimeError(f'Nie zwrócono trzech liczb!\n{debug}')
    if not subsequence(sorted(answer), sorted(arr)): raise RuntimeError(f'Nie zwrócono liczb z listy!\n{debug}')
    if sum(answer) > k: raise RuntimeError(f'Suma zwróconych liczb jest większa niż k!\n{debug}')
    print('OK!')

try:
    test([1, 2, 3], 7)
    test([1, 1, 1], 3)
    test([9, 8, 7, 6, 5, 4, 3, 2, 1], 6)
    test([9, 8, 7, 6, 5, 4, 3, 2, 1], 10)
    test([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5)
    test([9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9], 11)
except RuntimeError as e:
    print(e)
    import sys
    sys.exit()
print('Wszystkie testy zaliczone!')
