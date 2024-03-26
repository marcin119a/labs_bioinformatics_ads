from typing import List


def subset_sum(arr: List[int], k: int) -> bool:
    # Drugie zadanie z ćwiczeń (treść jest w pliku PDF).
    # TODO: uzupełnij tę funkcję.
    return True

# Testowanie.

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
