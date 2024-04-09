"""
\texttt{66, 11, 82, 36, 52, 7, 1, (?), 5, 4, 0, 91, 2, 6, (?), 8, 96, 9, 3, (?)}\\
Odpowiedzi: 36, 7, 8.\\
\texttt{59, 17, 48, (?), 76, 57, 46, 74, (?), 50, 46, 8, 99, 90, 40, (?), 63, 14, 57, 69, 87, 61, 85, 58, (?)}\\
Odpowiedzi: 48, 57, 50, 58.\\
"""

import heapq

class MedianFinder:
    #https://www.cs.usfca.edu/~galles/visualization/Heap.html
    def __init__(self):
        # Min-heap dla większych elementów
        self.minHeap = []
        # Max-heap dla mniejszych elementów (używamy negacji wartości, aby uzyskać max-heap)
        self.maxHeap = []

    def addNum(self, num):
        # Dodajemy do maxHeap, jeśli jest pusty lub num jest mniejsze od korzenia maxHeap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Balansowanie kopieców, tak aby różnica w ich wielkości nie przekraczała 1
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]

# Użycie
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Wypisuje 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Wypisuje 2
