def heapify(arr, n, i):
    largest = i  # Zakładamy, że obecny węzeł (i) jest największym
    l = 2 * i + 1  # lewy potomek
    r = 2 * i + 2  # prawy potomek

    # Jeśli lewy potomek istnieje i jest większy niż obecny największy, aktualizujemy largest
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Podobnie sprawdzamy prawego potomka
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Jeśli któryś z potomków był większy, zamieniamy i kontynuujemy heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Rekurencyjnie "naprawiamy" przesunięty w dół węzeł
        heapify(arr, n, largest)

# Przykład użycia funkcji heapify:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
# Budowanie kopca (od ostatniego węzła, który jest rodzicem, do korzenia)
for i in range(n // 2 - 1, -1, -1):
    print(arr)
    heapify(arr, n, i)

print("Stan tablicy po konstrukcji kopca max-heap:", arr)
