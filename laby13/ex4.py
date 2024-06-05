def KMPMatchAll(P, T):
    """Znajduje wszystkie wystąpienia wzorca P w tekście T i zwraca listę ich pozycji."""
    # Funkcja pomocnicza do obliczenia tablicy prefikso-sufiksów
    def computePSTable(P):
        m = len(P)
        PS = [0] * m
        j = 0
        for i in range(1, m):
            while (j > 0 and P[i] != P[j]):
                j = PS[j - 1]
            if P[i] == P[j]:
                j += 1
                PS[i] = j
        return PS

    # Obliczenie tablicy prefikso-sufiksów dla wzorca
    PS = computePSTable(P)
    n = len(T)
    m = len(P)
    q = 0  # Długość aktualnie dopasowanego fragmentu wzorca
    positions = []  # Lista pozycji, na których znajduje się wzorzec

    # Przeszukiwanie tekstu
    for i in range(n):
        while (q > 0 and P[q] != T[i]):
            q = PS[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            # Dopasowanie pełne wzorca P do tekstu T na pozycji i-m+1
            positions.append(i - m + 1)
            # Przygotowanie do szukania kolejnego wystąpienia
            q = PS[q - 1]

    return positions

# Przykładowe użycie:
pattern = "ab"
text = "abaabab"
print(KMPMatchAll(pattern, text))