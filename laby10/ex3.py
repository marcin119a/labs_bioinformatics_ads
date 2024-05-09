#https://visualgo.net/en/bst
class BSTNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.size_left = 0  # Liczba węzłów w lewym poddrzewie

class BSTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            v = self.root
            parent = None
            while v is not None:
                parent = v
                if key < v.key:
                    v = v.left
                    if v is None:
                        parent.left = BSTNode(key, parent)
                        self.update_sizes(parent.left)  # Aktualizuj rozmiar od nowego węzła
                else:
                    v = v.right
                    if v is None:
                        parent.right = BSTNode(key, parent)
                        self.update_sizes(parent.right)  # Aktualizuj rozmiar od nowego węzła

    def update_sizes(self, v):
        # Aktualizuj rozmiar w górę drzewa
        while v is not None:
            v.size_left = (v.left.size_left if v.left else 0) + (1 if v.left else 0)
            v = v.parent

    def find_by_order(self, i):
        v = self.root
        while v is not None:
            left_size = v.left.size_left if v.left else 0
            if i == left_size + 1:  # i-ty element to bieżący węzeł
                return v.key
            elif i <= left_size:  # i-ty element znajduje się w lewym poddrzewie
                v = v.left
            else:  # i-ty element znajduje się w prawym poddrzewie
                i -= left_size + 1
                v = v.right
        return None  # Jeśli i jest za duże

# Tworzenie przykładowego drzewa BST
bst = BSTree()
values_to_insert = [15, 10, 20, 8, 12, 16, 25]
for value in values_to_insert:
    bst.insert(value)

for i in range(1, len(values_to_insert) + 1):
    print(f"{i}-ty najmniejszy element: {bst.find_by_order(i)}")
