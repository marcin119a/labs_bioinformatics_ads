class BinNode:
    def __init__(self, valueA):
        self.valueA = valueA
        self.valueB = None
        self.left = None
        self.right = None


class BinTree:
    def __init__(self, root=None):
        self.root = root

    def average(self):
        # Funkcja pomocnicza, która przegląda drzewo i oblicza sumę oraz liczbę wierzchołków w poddrzewie
        def sum_and_count(node):
            if node is None:
                return (0, 0)
            left_sum, left_count = sum_and_count(node.left)
            right_sum, right_count = sum_and_count(node.right)
            total_sum = left_sum + right_sum + node.valueA
            total_count = left_count + right_count + 1
            node.valueB = total_sum / total_count  # Obliczenie średniej
            return (total_sum, total_count)

        # Rozpoczynamy przetwarzanie od korzenia
        sum_and_count(self.root)

# Tworzenie drzewa
root = BinNode(10)
root.left = BinNode(20)
root.right = BinNode(30)
root.left.left = BinNode(40)
root.left.right = BinNode(50)

tree = BinTree(root)
tree.average()

# Wyświetlenie wyników
def print_tree(node):
    if node is not None:
        print(f"ValueA: {node.valueA}, ValueB: {node.valueB}")
        print_tree(node.left)
        print_tree(node.right)

print_tree(root)
"""
         10
        /  \
       20   30
      /  \
     40  50

"""
