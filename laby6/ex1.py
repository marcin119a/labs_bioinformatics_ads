
def min_cost_cj(s: str, X: int, Y: int) -> int:
    cost = {'C': {'C': 0, 'J': X, '?': 0},
            'J': {'C': Y, 'J': 0, '?': 0},
            '?': {'C': 0, 'J': 0, '?': 0}
            }
    result = 0
    lastcj = s[0]
    for c in s[1:]:
        result += cost[lastcj][c]
        if c != '?':
            lastcj = c

    return result

# Testowanie.

assert min_cost_cj('CJ?CC?', 2, 3) == 5
assert min_cost_cj('CJ?CC?JJC??CJC??', 1, 4) == 15
assert min_cost_cj('????', 1, 2) == 0
assert min_cost_cj('CJ?CC?JJC??CJC??CCC??CCJJCJCJC', 2, 1) == 18

print('Wszystkie testy zaliczone!')