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
v = defaultdict(list)
for word in words:
    for i in range(len(word)):
        for letter in letters:
            similar_word = word[:i] + letter + word[i+1:]
            if similar_word in words_set and similar_word != word:
                v[word].append(similar_word)

# Mamy już graf; v['liver'] to lista wszystich poprawnych słów,
# które różnią się jedną literą od 'liver'.
# Konkretnie, v['liver'] = ['river', 'lover', 'lived', 'lives']

# TODO: wypisz najkrótszy możliwy ciąg słów zaczynający się od 'river',
# kończący się na 'water', w którym każde słowo różni się od poprzedniego
# tylko na jednej pozycji.
