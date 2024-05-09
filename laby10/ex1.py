def count_sort_by_length(strings):
    # Znajdź maksymalną długość napisu w liście
    max_length = 0
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)

    # Inicjalizuj tablicę zliczającą
    count = [0] * (max_length + 1)

    # Zlicz długości napisów
    for s in strings:
        count[len(s)] += 1

    # Kumuluj wartości w tablicy zliczającej
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Tworzymy tablicę wynikową
    output = [None] * len(strings)

    # Umieszczanie napisów w odpowiednich miejscach w tablicy wynikowej
    for s in reversed(strings):  # Iterujemy od końca dla zachowania stabilności
        count[len(s)] -= 1
        output[count[len(s)]] = s

    return output

# Przykład użycia
strings = ["hello", "world", "a", "ab", "abc", "abcd"]
sorted_strings = count_sort_by_length(strings)
print(sorted_strings)
