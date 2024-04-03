
def min_cost_cj(s: str, X: int, Y: int) -> int:
    # Drugie zadanie z ćwiczeń (treść jest w pliku PDF).
    # TODO: uzupełnij tę funkcję.
    return 0   


# Testowanie.

assert min_cost_cj('CJ?CC?', 2, 3) == 5
assert min_cost_cj('CJ?CC?JJC??CJC??', 1, 4) == 15
assert min_cost_cj('????', 1, 2) == 0
assert min_cost_cj('CJ?CC?JJC??CJC??CCC??CCJJCJCJC', 2, 1) == 18
assert min_cost_cj('??CJ??J??C?J??CCJJ??', 5, -2) == 7
assert min_cost_cj('????', -1, -2) == -5

print('Wszystkie testy zaliczone!')