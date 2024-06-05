from collections import defaultdict
from string import ascii_lowercase as letters

# Wczytujemy słowa z pliku.
words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line.strip())
assert all(len(w) == 5 for w in words)

# Przyda nam się zbiór słów, żeby sprawdzać, czy słowo do niego należy w czasie O(1).
words_set = set(words)

# Budujemy graf w czasie O(n), gdzie n to liczba słów.
# (ale to trochę oszustwo; wykonujemy co najmniej n*5*26*5 = 650n operacji)

from collections import defaultdict, deque
v = defaultdict(list)
for word in words:
    for i in range(len(word)):
        for letter in letters:
            similar_word = word[:i] + letter + word[i + 1:]
            if similar_word in words_set and similar_word != word:
                v[word].append(similar_word)


def bfs_shortest_path(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_word, path = queue.popleft()

        if current_word == goal:
            return path

        visited.add(current_word)

        for neighbor in v[current_word]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None
path = bfs_shortest_path('river', 'water')
if path:
    print("Najkrótsza ścieżka z 'river' do 'water':")
    for word in path:
        print(word)
else:
    print("Nie znaleziono ścieżki z 'river' do 'water'.")

