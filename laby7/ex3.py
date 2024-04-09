"""
Jak ˛a złozono ˙ s´c czasow ˛a ma sortowanie (leksykograficzne) listy napisów?\
"""
"""
https://visualgo.net/en/sorting
"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Zliczanie wystąpień cyfr na pozycji exp
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Akumulacja, aby znać końcowe pozycje cyfr w output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Budowanie tablicy wyjściowej
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Kopiowanie posortowanej tablicy do arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Znajdowanie maksymalnej liczby, aby poznać liczbę cyfr
    max_val = max(arr)

    # Sortowanie dla każdej cyfry
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Przykładowe użycie
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
