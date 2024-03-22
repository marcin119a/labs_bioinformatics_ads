from typing import Any, Dict, List, Optional

class PosNode:
    value: Any
    children: Dict[Any, 'PosNode']

    # Uwaga! Podawanie słownika/listy jako domyślnej wartości argumentu (children = {})
    # może łatwo doprowadzić do dziwnych błędów, lepiej tego unikać.
    def __init__(self, value: Any, children: Dict[Any, 'PosNode'] = {}):
        self.value = value
        self.children = children
    def value_at_adress(self, adress: List[Any]):
        if len(adress) == 0: return self.value
        label = adress[0]
        if label not in self.children: return None
        child = self.children[label]
        return child.value_at_adress(adress[1:])
class PosTree:
    root: Optional[PosNode]
    def __init__(self, node: Optional[PosNode] = None):
        self.root = node

    def value_at_address(self, address: List[Any]) -> Any:
        # TODO: uzupełnij tę funkcję.
        if self.root is None:
            return None
        node = self.root
        for label in address:
            if label not in node.children: return None
            node = node.children[label]
        return node.value

        # Powinna zwracać wartość wierzchołka o adresie "address" w drzewie
        # (lub None, jeśli nie istnieje wierzchołek o takim adresie).
    def value_at_adress(self, address: List[Any]):
        if self.root is None: return None
        return self.root.value_at_adress(address)



# Testowanie.

Tree, Node = PosTree, PosNode

lecture_example1 = Tree(
    Node('temperatura', {
        'wysoka': Node('tętno', {
            'słabe': Node('grypa'),
            'silne': Node('dżuma')
        }),
        'normalna': Node('tętno', {
            'słabe': Node('trądzik lub krup'),
            'silne': Node('stan normalny')
        }),
        'niska': Node('tętno', {
            'słabe': Node('kolor skóry', {
                'zarumieniona': Node('epizootia'),
                'normalna': Node('grypa'),
                'woskowa': Node('martwy')
            }),
            'silne': Node('opryszczka')
        })
    })
)
assert lecture_example1.value_at_address(['wysoka', 'silne']) == 'dżuma'
assert lecture_example1.value_at_address(['normalna', 'słabe']) == 'trądzik lub krup'
assert lecture_example1.value_at_address(['niska']) == 'tętno'
assert lecture_example1.value_at_address(['niska', 'słabe', 'woskowa']) == 'martwy'
assert lecture_example1.value_at_address([]) == 'temperatura'
assert lecture_example1.value_at_address(['niebotyczna']) == None
assert lecture_example1.value_at_address(['niska', 'słabe', 'zielona']) == None


lecture_example2 = Tree(
    Node('', {
        'a': Node('a', {
            'a': Node('aa'),
            'b': Node('ab', {
                'a': Node('aba'),
                'b': Node('abb')
            })
        }),
        'b': Node('b', {
            'a': Node('ba', {
                'a': Node('baa'),
                'b': Node('bab')
            }),
            'b': Node('bb')
        })
    })
)

assert lecture_example2.value_at_address(['a', 'a']) == 'aa'
assert lecture_example2.value_at_address([]) == ''
assert lecture_example2.value_at_address(['b', 'a', 'b']) == 'bab'
assert lecture_example2.value_at_address(['a', 'b', 'b']) == 'abb'
assert lecture_example2.value_at_address(['b', 'b', 'a']) == None
assert lecture_example2.value_at_address(['b', 'b', 'a', 'a']) == None

empty = Tree()
assert empty.value_at_address([]) == None
assert empty.value_at_address(['abc']) == None

onevertex = Tree(Node(5))
assert onevertex.value_at_address([]) == 5
assert onevertex.value_at_address([5]) == None

star = Tree(
    Node('root', {
        0: Node('first'),
        1: Node('second'),
        2: Node('third')
    })
)
assert star.value_at_address([]) == 'root'
assert star.value_at_address([0]) == 'first'
assert star.value_at_address([1]) == 'second'
assert star.value_at_address([2]) == 'third'
assert star.value_at_address([3]) == None

print('Wszystkie testy zaliczone!')
