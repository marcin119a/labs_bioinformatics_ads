def local_alignment(seq1, seq2, sim):
    # Inicjalizacja tablicy dynamicznej
    m = len(seq1)
    n = len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Zmienne przechowujące pozycję najlepszego dopasowania
    max_score = 0
    max_i = 0
    max_j = 0

    # Wypełnianie tablicy dynamicznej
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(
                dp[i - 1][j - 1] + sim(seq1[i - 1], seq2[j - 1]),  # Dopasowanie
                dp[i - 1][j],  # Luka w pierwszej sekwencji
                dp[i][j - 1],  # Luka w drugiej sekwencji
                0  # Rozpoczęcie nowego uliniowienia
            )
            # Aktualizacja pozycji najlepszego dopasowania
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_i = i
                max_j = j
    print(dp)
    # Odtworzenie uliniowienia od pozycji najlepszego dopasowania
    alignment_seq1 = ''
    alignment_seq2 = ''
    i, j = max_i, max_j
    while i > 0 and j > 0 and dp[i][j] > 0:
        if dp[i][j] == dp[i - 1][j - 1] + sim(seq1[i - 1], seq2[j - 1]):
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = '-' + alignment_seq2
            i -= 1
        else:
            alignment_seq1 = '-' + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            j -= 1

    return alignment_seq1, alignment_seq2, max_score


# Przykładowa funkcja podobieństwa
def sim(x, y):
    if x == y:
        return 2
    else:
        return -2


# Przykładowe sekwencje DNA
seq1 = 'TGC'
seq2 = 'ATG'

# Znalezienie optymalnego uliniowienia lokalnego
alignment_seq1, alignment_seq2, score = local_alignment(seq1, seq2, sim)

print("Optymalne uliniowienie lokalne:")
print(alignment_seq1)
print(alignment_seq2)
print("Wynik:", score)
