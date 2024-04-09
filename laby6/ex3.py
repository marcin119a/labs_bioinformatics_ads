from typing import List

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]    # Takie mamy monety w Polsce (wszystkie wartości są wyrażone w groszach).

def change_combination_count(coins: List[int], change: int) -> int:
    dp = [1] + [0] * change
    for coin in coins:
        for kwota_czesciowa in range(change+1):
            if kwota_czesciowa + coin <= change:
                dp[kwota_czesciowa + coin] += dp[kwota_czesciowa]

    return dp[change]


# Testowanie.

change_combination_count(coins, 10)
#assert change_combination_count(coins, 13) == 16
#assert change_combination_count(coins, 26) == 75
#assert change_combination_count(coins, 100) == 4563
#assert change_combination_count(coins, 1000) == 327631321

print('Wszystkie testy zaliczone!')
