def Wypłać(kwota, banknoty):
    n = len(banknoty)
    # tablica dp przechowuje minimalną liczbę banknotów potrzebnych do uzyskania każdej kwoty od 0 do kwota
    dp = [float('inf')] * (kwota + 1)
    dp[0] = 0  # 0 banknotów jest potrzebnych do uzyskania kwoty 0

    # przechowujemy indeksy banknotów użytych do złożenia kwot
    wybrane_banknoty = [-1] * (kwota + 1)

    # wypełniamy tabelę dp
    for i in range(1, kwota + 1):
        for j in range(n):
            if banknoty[j] <= i and dp[i - banknoty[j]] + 1 < dp[i]:
                dp[i] = dp[i - banknoty[j]] + 1
                wybrane_banknoty[i] = j

    # jeśli dp[kwota] jest nieskończoność, oznacza to, że nie można złożyć kwoty
    if dp[kwota] == float('inf'):
        return None

    # odtwarzamy użyte banknoty
    wynik = []
    while kwota > 0:
        if wybrane_banknoty[kwota] == -1:
            return None
        wynik.append(wybrane_banknoty[kwota])
        kwota -= banknoty[wybrane_banknoty[kwota]]

    # wynik może być w dowolnej kolejności, zależy od tego, jakiego kolejności potrzebujemy
    return wynik[::-1]  # zwracamy odwróconą listę, aby mieć kolejność wydawania

# Przykładowe użycie funkcji
print(Wypłać(7, [1, 2, 5]))  # zwróci [2, 1, 0] lub inną poprawną kombinację
print(Wypłać(4, [3, 5]))    # zwróci None, ponieważ nie można uzyskać kwoty 4
