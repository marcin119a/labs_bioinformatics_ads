from typing import List

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]    # Takie mamy monety w Polsce (wszystkie wartości są wyrażone w groszach).

def change_combination_count(coins: List[int], change: int) -> int:
    # Trzecie zadanie z ćwiczeń (treść jest w pliku PDF).
    # TODO: uzupełnij tę funkcję.
    return 0


# Testowanie.

assert change_combination_count(coins, 10) == 11
assert change_combination_count(coins, 13) == 16
assert change_combination_count(coins, 26) == 75
assert change_combination_count(coins, 100) == 4563
assert change_combination_count(coins, 1000) == 327631321

print('Wszystkie testy zaliczone!')
