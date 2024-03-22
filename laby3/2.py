from typing import Any, List, Optional

class PosBinNode:
    value: Any
    left: Optional['PosBinNode']
    right: Optional['PosBinNode']

    def __init__(self,
                 value: Any,
                 left: Optional['PosBinNode'] = None,
                 right: Optional['PosBinNode'] = None):
        self.value = value
        self.left = left
        self.right = right

    def subtree_values_inorder(self) -> List[Any]:
        if self.left is None and self.right is None:
            return [self.value]
        if self.left is None and self.right is not None:
            return [self.value] + self.right.subtree_values_inorder()
        if self.left is not None and self.right is None:
            return self.left.subtree_values_inorder() + [self.value]
        if self.left is not None and self.right is not None:
            return self.left.subtree_values_inorder() + [self.value] + self.right.subtree_values_inorder()
        return []

    def subtree_values_inorder2(self, values: List[Any]) -> List[Any]:
        if self.left is not None:
            self.left.subtree_values_inorder2(values)
        values.append(self.value)
        if self.right is not None:
            self.right.subtree_values_inorder2(values)

class PosBinTree:
    root: Optional[PosBinNode]
    def __init__(self, node: Optional[PosBinNode] = None):
        self.root = node

    def values_inorder(self) -> List[Any]:
       if self.root is None: return []
       values = []
       self.root.subtree_values_inorder2(values)
       return values

# Testowanie.

Tree, Node = PosBinTree, PosBinNode

# Pełne drzewo o wysokości 2.
fullh2 = Tree(
    Node('RootValue',
        Node(
            'LeftChildValue',
                None,
                Node('LeftRightGrandchildValue')
        ),
        Node(
            'RightChildValue',
                Node('RightLeftGrandchildValue'),
                None
        )
    )
)
assert fullh2.values_inorder() == ['LeftChildValue', 'LeftRightGrandchildValue', 'RootValue', 'RightLeftGrandchildValue', 'RightChildValue']

# Ścieżka w lewo z czterema wierzchołkami.
pathl4 = Tree(
    Node('First',
        Node('Second',
            Node('Third',
                Node('Fourth'))))
)

assert pathl4.values_inorder() == ['Fourth', 'Third', 'Second', 'First']

# Ścieżka w prawo z czterema wierzchołkami.
pathr4 = Tree(
    Node('First',
        None,
        Node('Second',
            None,
            Node('Third',
                None,
                Node('Fourth'))))
)
assert pathr4.values_inorder() == ['First', 'Second', 'Third', 'Fourth']

# Puste drzewo.
empty = Tree()
assert empty.values_inorder() == []

# Drzewo z jednym wierzchołkiem.
onevertex = Tree(Node(5))   # Wartości w wierzchołkach nie muszą być napisami.
assert onevertex.values_inorder() == [5]

print('Wszystkie testy zaliczone!')
