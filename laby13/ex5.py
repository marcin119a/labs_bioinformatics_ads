from collections import defaultdict

def PSTable(P):
    """Tworzy tablicę prefikso-sufiksów dla wzorca P."""
    m = len(P)
    PS = [-1] * (m + 1)  # Rozszerzona tablica PS
    k = 0  # Długość aktualnie najdłuższego dopasowanego prefikso-sufiksu
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = PS[k]
        if P[k] == P[i]:
            k += 1
        PS[i + 1] = k
    return PS

def ComputeDelta(P):
    """Buduje funkcję przejścia automatu na podstawie wzorca P."""
    Sigma = set(P)  # Zbiór znaków występujących we wzorcu
    m = len(P)
    delta = defaultdict(int)
    PS = PSTable(P)

    for q in range(m + 1):
        for x in Sigma:
            if q < m and x == P[q]:
                delta[q, x] = q + 1
            else:
                k = PS[q]  # Używamy PS do znalezienia odpowiedniego stanu po nieudanym dopasowaniu
                while k > 0 and (k >= m or P[k] != x):
                    k = PS[k]
                delta[q, x] = k + 1 if k >= 0 and k < m and P[k] == x else 0

    return delta
