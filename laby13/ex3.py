def PSTable(P):
   PS = [-1]
   q = -1
   for x in P:
      while q >= 0 and P[q]!=x:
         q = PS[q]
      q += 1
      PS.append(q)
   return PS

def KMPMatch(P, T):
    PS = PSTable(P + "#" + T)
    m = len(P)
    results = []
    for i in range(len(PS)):
        # Szukamy wystąpienia długości wzorca w tablicy PS, począwszy od indeksu po #,
        # co odpowiada rozpoczęciu porównań w tekście T.
        if PS[i] == m:
            # Dodajemy miejsce wystąpienia wzorca w tekście, biorąc pod uwagę długość wzorca oraz separator.
            results.append(i - 2 * m)
    return results
