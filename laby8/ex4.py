def NajlepszaDroga(Plansza):
    m = len(Plansza)
    n = len(Plansza[0])

    # Inicjalizacja tablicy dp wartościami nieskończonymi
    dp = [[float('inf')] * n for _ in range(m)]

    # Punkt startowy
    dp[0][0] = 0

    # Wypełnianie tablicy dp
    for i in range(m):
        for j in range(n):
            if i > 0:
                # Sprawdzamy, czy zmienia się kolor
                if Plansza[i][j] != Plansza[i - 1][j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j > 0:
                # Sprawdzamy, czy zmienia się kolor
                if Plansza[i][j] != Plansza[i][j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])

    # Wynik znajduje się w prawym górnym rogu
    return dp[m - 1][n - 1]


# Przykład użycia
Plansza = [
    ['czerwony', 'niebieski', 'niebieski'],
    ['czerwony', 'zielony', 'zielony'],
    ['czerwony', 'zielony', 'niebieski']
]
print(NajlepszaDroga(Plansza))
