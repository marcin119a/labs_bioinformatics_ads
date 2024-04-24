def global_alignment_cost(seq1, seq2, sim):
    # Inicjalizacja tablicy dynamicznej
    m = len(seq1)
    n = len(seq2)
    dp = [[-float('inf')] * (n + 1) for _ in range(2)]
    dp[0][0] = 0

    # Wypełnienie pierwszego wiersza
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] - gap_penalty('-', seq2[j - 1])

    # Obliczanie kosztów optymalnego uliniowienia
    for i in range(1, m + 1):
        dp[i % 2][0] = dp[(i - 1) % 2][0] - gap_penalty(seq1[i - 1], '-')
        for j in range(1, n + 1):
            dp[i % 2][j] = max(
                dp[(i - 1) % 2][j - 1] + sim(seq1[i - 1], seq2[j - 1]),  # Dopasowanie
                dp[(i - 1) % 2][j] - gap_penalty(seq1[i - 1], '-'),  # Luka w pierwszej sekwencji
                dp[i % 2][j - 1] - gap_penalty('-', seq2[j - 1])  # Luka w drugiej sekwencji
            )
    print(dp)
    # Znalezienie kosztu optymalnego uliniowienia
    return dp[m % 2][n]


# Przykładowa funkcja podobieństwa
def sim(x, y):
    if x == y:
        return 2
    else:
        return -3


# Funkcja określająca karę za wstawienie luki
def gap_penalty(a, b):
    return 2  # Za wstawienie luki kara wynosi 2


# Przykładowe sekwencje DNA
seq1 = 'TGC'
seq2 = 'ATG'

# Znalezienie kosztu optymalnego uliniowienia globalnego
cost = global_alignment_cost(seq1, seq2, sim)

print("Koszt optymalnego uliniowienia globalnego:", cost)
