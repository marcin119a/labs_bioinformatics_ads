class Queue:
    def __init__(self):
        self.L = []  # Lista przechowująca elementy kolejki
        self.beg = 0  # Indeks pierwszego elementu kolejki

    def append(self, item):
        self.L.append(item)  # Dodajemy element na koniec listy

    def extract(self):
        if self.empty():
            raise Exception("Queue is empty")
        item = self.L[self.beg]  # Pobieramy element z początku kolejki
        self.beg += 1  # Zwiększamy indeks początku kolejki
        return item

    def empty(self):
        return self.beg >= len(self.L)  # Sprawdzamy, czy indeks początku przekroczył długość listy

# Użycie
queue = Queue()
queue.append(1)
queue.append(2)
print(queue.extract())  # Wypisuje 1
print(queue.extract())  # Wypisuje 2
