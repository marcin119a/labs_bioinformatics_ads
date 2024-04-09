#https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
"""
Zasymuluj działanie kolejki priorytetowej typu MAX z wykładu (korzystajacej z
kopca binarnego) dla nastepujacego ci ˛agu operacji:
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PQueue:
   def __init__(self, L):
      self.heap = [None]  # Pierwszy element to None dla łatwiejszego indeksowania
      self.heap.extend(L)  # Rozszerzenie kopca elementami z L
      r = len(self.heap) // 2
      for i in range(r, 0, -1):
         self.down_heap(i)

   def up_heap(self, i):
      # Przesuwanie elementu w górę kopca do momentu, aż będzie mniejszy od swojego rodzica
      while i > 1 and self.heap[i] > self.heap[self.parent(i)]:
         self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]  # Zamiana z rodzicem
         i = self.parent(i)  # Aktualizacja indeksu do dalszego porównywania

   def down_heap(self, i):
      # Przesuwanie elementu w dół kopca do momentu, aż będzie większy od swoich dzieci
      while True:
         max_el = i
         for j in (self.left(i), self.right(i)):  # Sprawdzenie lewego i prawego dziecka
            if j < len(self.heap) and self.heap[j] > self.heap[max_el]:
               max_el = j
         if max_el != i:
            self.heap[i], self.heap[max_el] = self.heap[max_el], self.heap[i]  # Zamiana z większym dzieckiem
            i = max_el
         else:
            break

   def insert(self, x):
      # Dodanie nowego elementu do kopca i przesunięcie go w górę do odpowiedniego miejsca
      self.heap.append(x)
      self.up_heap(len(self.heap) - 1)

   def increase(self, i, x):
      # Zwiększenie wartości elementu i przesunięcie go w górę kopca
      self.heap[i] = x
      self.up_heap(i)

   def find_max(self):
      # Znalezienie i zwrócenie maksymalnego elementu w kopcu
      return self.heap[1]

   def replace_max(self, x):
      # Zamiana maksymalnego elementu z nowym i przesunięcie nowego elementu w dół kopca
      x, self.heap[1] = self.heap[1], x
      self.down_heap(1)
      return x

   def extract_max(self):
      # Usunięcie i zwrócenie maksymalnego elementu z kopca
      x = self.heap.pop()
      if len(self.heap) > 1:
         return self.replace_max(x)
      else:
         return x

   # Metody pomocnicze dla łatwiejszego obliczania indeksów rodziców i dzieci
   def parent(self, i):
      return i // 2

   def left(self, i):
      return 2 * i

   def right(self, i):
      return 2 * i + 1


from random import shuffle
R = list(range(10))
print(R)
shuffle(R)
print(R)
Q = PQueue(R)
print(Q.heap)
print(Q.extract_max())
print(Q.heap)
print(Q.find_max())
Q.insert(9)
print(Q.heap)


def heap_sort(L):
   pq = PQueue(L)
   sorted_list = []
   while len(pq.heap) > 1:  # Dopóki kopiec ma więcej niż jeden element (pamiętajmy o None na początku)
      sorted_list.append(pq.extract_max())  # Usuwamy maksymalny element i dodajemy go do posortowanej listy
   return sorted_list[::-1]  # Odwracamy listę, ponieważ usunęliśmy elementy od największego do najmniejszego

unsorted_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
sorted_list = heap_sort(unsorted_list)
print(sorted_list)