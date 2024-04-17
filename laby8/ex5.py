def LiczbaDrog(Plansza):
    m = len(Plansza)
    n = len(Plansza[0])

    # Tworzymy tablicę dp, gdzie dp[i][j] oznacza liczbę ścieżek do punktu (i, j)
    dp = [[0] * n for _ in range(m)]

    # Początkowy punkt ma jedną możliwą ścieżkę (zakładając, że zaczynamy na tym polu)
    dp[0][0] = 1

    # Wypełnianie tablicy dp
    for i in range(m):
        for j in range(n):
            # Sprawdzamy możliwość przejścia w dół
            if i + 1 < m and Plansza[i + 1][j] != Plansza[i][j]:
                dp[i + 1][j] += dp[i][j]

            # Sprawdzamy możliwość przejścia w prawo
            if j + 1 < n and Plansza[i][j + 1] != Plansza[i][j]:
                dp[i][j + 1] += dp[i][j]

    # Wynik znajduje się w prawym górnym rogu
    return dp[m - 1][n - 1]


# Przykład użycia
Plansza = [
    ['czerwony', 'niebieski', 'niebieski'],
    ['czerwony', 'zielony', 'zielony'],
    ['czerwony', 'zielony', 'niebieski']
]
print(LiczbaDrog(Plansza))
