from typing import List, Tuple


def maximal_number_of_segments(segments: List[Tuple[int, int]]) -> int:
    # Czwarte zadanie z ćwiczeń (treść jest w pliku PDF).
    # TODO: uzupełnij tę funkcję.
    return 0


# Testowanie.

f = maximal_number_of_segments  # Krótsza nazwa, dla wygody.

assert f([]) == 0

assert f([(0, 5), (2, 7), (4, 6)]) == 1  # Wszystkie odcinki się nakładają.

assert f([(0, 2), (2, 4)]) == 1 # Wybrane odcinki nie mogą się stykać końcami!

assert f([(1, 10), (2, 4), (6, 8)]) == 2    # Możemy wziąć odcinki (2, 4) i (6, 8).

assert f([(90, 110), (95, 115), (85, 105), (1, 100), (101, 200)]) == 2  # Możemy wziąć odcinki (1, 100) i (101, 200). (nie opłaca się brać krótkich odcinków!)

# Losowe testy.

assert f([(9, 10), (1, 2), (6, 8), (8, 10), (5, 10), (5, 6), (4, 8), (7, 8)]) == 4
# Przykładowe rozwiązanie: (1, 2), (5, 6), (7, 8), (9, 10).

assert f([(9, 10), (2, 7), (5, 8), (4, 9), (7, 10), (6, 8), (4, 6), (8, 10), (3, 10), (2, 10), (7, 9), (4, 5), (5, 10), (8, 9), (4, 8), (6, 9), (4, 7)]) == 3
# Przykładowe rozwiązanie: (4, 5), (6, 8), (9, 10).

assert f([(81, 82), (17, 46), (34, 62), (64, 75), (47, 62), (90, 97), (68, 100), (21, 22), (22, 23), (95, 96), (27, 71), (22, 38), (9, 81), (91, 92), (18, 59), (45, 49), (52, 88), (74, 88), (30, 51), (96, 100), (81, 96), (72, 87), (16, 40), (35, 41), (59, 69), (72, 90), (17, 69), (37, 87), (30, 72), (52, 84), (21, 54), (83, 93), (46, 80), (88, 89), (76, 93), (85, 93), (68, 89), (71, 79), (26, 89), (98, 99), (7, 24), (36, 60), (31, 33), (95, 97), (10, 13), (8, 80), (2, 9), (3, 47), (38, 72), (34, 59)]) == 13
# Przykładowe rozwiązanie: (2, 9), (10, 13), (21, 22), (31, 33), (35, 41), (45, 49), (59, 69), (71, 79), (81, 82), (88, 89), (91, 92), (95, 96), (98, 99).

print('Wszystkie testy zaliczone!')
