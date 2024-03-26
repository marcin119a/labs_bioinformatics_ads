from typing import Any, Optional

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

class PosBinTree:
    root: Optional[PosBinNode]
    def __init__(self, node: Optional[PosBinNode] = None):
        self.root = node


def find_value_on_first_two_levels(tree: PosBinTree, value: Any) -> bool:
    if tree.root is None:
        return False
    if tree.root.value == value:
        return True
    if tree.root.left is not None:
        if tree.root.left.value == value:
            return True
    if tree.root.right is not None:
        if tree.root.right.value == value:
            return True
    return False

    # TODO: uzupełnij tę funkcję.
    # Powinna zwracać True, jeśli na pierwszych dwóch poziomach drzewa (czyli: w korzeniu lub
    # którymkolwiek dziecku korzenia) istnieje wierzchołek o wartości value, lub False w przeciwnym przypadku.
    return False



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
assert find_value_on_first_two_levels(fullh2, 'RootValue') == True
assert find_value_on_first_two_levels(fullh2, 'LeftChildValue') == True
assert find_value_on_first_two_levels(fullh2, 'RightChildValue') == True
assert find_value_on_first_two_levels(fullh2, 'LeftRightGrandchildValue') == False
assert find_value_on_first_two_levels(fullh2, 'RightLeftGrandchildValue') == False

# Ścieżka w lewo z czterema wierzchołkami.
pathl4 = Tree(
    Node('First',
        Node('Second',
            Node('Third',
                Node('Fourth'))))
)

assert find_value_on_first_two_levels(pathl4, 'First') == True
assert find_value_on_first_two_levels(pathl4, 'Second') == True
assert find_value_on_first_two_levels(pathl4, 'Third') == False
assert find_value_on_first_two_levels(pathl4, 'Fourth') == False
assert find_value_on_first_two_levels(pathl4, None) == False

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
assert find_value_on_first_two_levels(pathr4, 'First') == True
assert find_value_on_first_two_levels(pathr4, 'Second') == True
assert find_value_on_first_two_levels(pathr4, 'Third') == False
assert find_value_on_first_two_levels(pathr4, 'Fourth') == False
assert find_value_on_first_two_levels(pathr4, None) == False

# Puste drzewo.
empty = Tree()
assert find_value_on_first_two_levels(empty, 'whatever') == False
assert find_value_on_first_two_levels(empty, None) == False

# Drzewo z jednym wierzchołkiem.
onevertex = Tree(Node(5))   # Wartości w wierzchołkach nie muszą być napisami.
assert find_value_on_first_two_levels(onevertex, 5) == True
assert find_value_on_first_two_levels(onevertex, 4) == False
assert find_value_on_first_two_levels(onevertex, '5') == False

print('Wszystkie testy zaliczone!')
