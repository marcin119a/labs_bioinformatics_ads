class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_start_index = float('inf')  # przechowuje najmniejszy indeks startowy sufiksu w węźle

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, start_index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.min_start_index = min(node.min_start_index, start_index)
        node.children['$'] = TrieNode()  # Końcowy znak dla oznaczenia końca słowa
        node.children['$'].min_start_index = start_index  # Ustawienie indeksu na końcu słowa

    def build_suffix_tree(self, s):
        # Dodaje wszystkie sufiksy słowa s do drzewa sufiksowego
        for i in range(len(s)):
            self.insert(s[i:], i)

    def find_first_occurrence(self, pattern):
        # Szuka pierwszego wystąpienia wzorca pattern w drzewie sufiksowym
        node = self.root
        for char in pattern:
            if char in node.children:
                node = node.children[char]
            else:
                return -1  # Wzorzec nie istnieje w drzewie
        # Jeśli wzorzec istnieje, zwraca najmniejszy indeks startowy zapisany w odpowiednim węźle
        return node.min_start_index