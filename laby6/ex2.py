
def min_cost_cj(s: str, X: int, Y: int) -> int:
    #dp[i][X] - najlepszy możliwy koszt dla napisu s[:i+1] oraz kończącej się na literze X
    #min (dp[n-1]['J'], dp[n-1]['C'])
    inf = float('infinity')
    n = len(s)
    dp = [{'C': inf, 'J': inf}]

    if s[0] == 'C':
        dp[0]['C'] = 0
        dp[0]['J'] = inf
    if s[0] == 'J':
        dp[0]['C'] = inf
        dp[0]['J'] = 0
    if s[0] == '?':
        dp[0]['C'] = 0
        dp[0]['J'] = 0
    # Mozna odkomentować ponizszy print w celu inspekcji zmian tablicy dp
    # print(f's[0] = {s[0]}, dp[0] = {dp[0]}')

    # Kluczowa sprawa: znając dp[i-1] (tzn. dp[i-1]['C'] i dp[i-1]['J']) i znak s[i], umiemy wyliczyć dp[i].
    for i, c in enumerate(s[1:], 1):
        dp.append({'C': inf, 'J': inf})
        if c == 'C':
            dp[i]['C'] = min(dp[i - 1]['C'], dp[i - 1]['J'] + Y)
            dp[i]['J'] = inf
        if c == 'J':
            dp[i]['C'] = inf
            dp[i]['J'] = min(dp[i - 1]['C'] + X, dp[i - 1]['J'])
        if c == '?':
            dp[i]['C'] = min(dp[i - 1]['C'], dp[i - 1]['J'] + Y)
            dp[i]['J'] = min(dp[i - 1]['C'] + X, dp[i - 1]['J'])
        # Mozna odkomentować ponizszy print w celu inspekcji zmian tablicy dp
        # print(f's[{i}] = {s[i]}, dp[{i}] = {dp[i]}')

    return min(dp[n - 1]['C'], dp[n - 1]['J'])


# Testowanie.

assert min_cost_cj('CJ?CC?', 2, 3) == 5
assert min_cost_cj('CJ?CC?JJC??CJC??', 1, 4) == 15
assert min_cost_cj('????', 1, 2) == 0
assert min_cost_cj('CJ?CC?JJC??CJC??CCC??CCJJCJCJC', 2, 1) == 18
assert min_cost_cj('??CJ??J??C?J??CCJJ??', 5, -2) == 7
assert min_cost_cj('????', -1, -2) == -5

print('Wszystkie testy zaliczone!')