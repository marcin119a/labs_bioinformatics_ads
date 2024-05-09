def global_alignment(seq1, seq2, sim):
    # Inicjalizacja tablicy dynamicznej
    m = len(seq1)
    n = len(seq2)
    dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    # Wypełnienie pierwszego wiersza i pierwszej kolumny
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] - gap_penalty(seq1[i - 1], '-')
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] - gap_penalty('-', seq2[j - 1])
    # Wypełnianie reszty tablicy dynamicznej
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(
                dp[i - 1][j - 1] + sim(seq1[i - 1], seq2[j - 1]),  # Dopasowanie
                dp[i - 1][j] - gap_penalty(seq1[i - 1], '-'),  # Luka w pierwszej sekwencji
                dp[i][j - 1] - gap_penalty('-', seq2[j - 1])  # Luka w drugiej sekwencji
            )
    print(dp)

    # Odtworzenie optymalnego uliniowienia
    alignment_seq1 = ''
    alignment_seq2 = ''
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] - gap_penalty(seq1[i - 1], '-'):
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = '-' + alignment_seq2
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] - gap_penalty('-', seq2[j - 1]):
            alignment_seq1 = '-' + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            j -= 1
        else:
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            i -= 1
            j -= 1

    return alignment_seq1, alignment_seq2


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

# Znalezienie optymalnego globalnego uliniowienia
alignment_seq1, alignment_seq2 = global_alignment(seq1, seq2, sim)

print("Globalne uliniowienie:")
print(alignment_seq1)
print(alignment_seq2)
