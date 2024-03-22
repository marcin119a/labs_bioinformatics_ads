from typing import Any, Dict, List, Optional

class PosNode:
    value: Any
    children: Dict[Any, 'PosNode']

    # Uwaga! Podawanie słownika/listy jako domyślnej wartości argumentu (children = {})
    # może łatwo doprowadzić do dziwnych błędów, lepiej tego unikać.
    def __init__(self, value: Any, children: Dict[Any, 'PosNode'] = {}):
        self.value = value
        self.children = children

class PosTree:
    root: Optional[PosNode]
    def __init__(self, node: Optional[PosNode] = None):
        self.root = node

    def all_addresses(self) -> List[List[Any]]:
        # TODO: uzupełnij tę funkcję.
        # Powinna zwracać listę wszystkich adresów w drzewie (w dowolnej kolejności).
        if self.root is None: return []
        result: List[Any] = []

        def add_adresses_in_subtree(node: PosNode, current_adress: List[Any]):
            result.append(current_adress)
            for label, child in node.children.items():
                child_adresses = current_adress + [label]
                add_adresses_in_subtree(child, child_adresses)
        add_adresses_in_subtree(self.root, [])

        return result



# Testowanie.

Tree, Node = PosTree, PosNode

empty = Tree()
assert empty.all_addresses() == []

onevertex = Tree(Node(5))
assert onevertex.all_addresses() == [[]]

# Ignorujemy kolejność adresów -- zamieniamy listę na zbiór.
# W tym celu musimy też zamienić wewnętrzne listy na tuple.
def same_addresses(list1: List[List[Any]], list2: List[List[Any]]):
    return {tuple(x) for x in list1} == {tuple(x) for x in list2}

star = Tree(
    Node('root', {
        0: Node('first'),
        1: Node('second'),
        2: Node('third')
    })
)
assert same_addresses(star.all_addresses(), [[], [0], [1], [2]])


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
assert same_addresses(lecture_example1.all_addresses(), 
    [
        [],
            ['wysoka'],
                ['wysoka', 'słabe'],
                ['wysoka', 'silne'],
            ['normalna'],
                ['normalna', 'słabe'],
                ['normalna', 'silne'],
            ['niska'],
                ['niska', 'słabe'],
                    ['niska', 'słabe', 'zarumieniona'],
                    ['niska', 'słabe', 'normalna'],
                    ['niska', 'słabe', 'woskowa'],
                ['niska', 'silne']
    ])


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

assert same_addresses(lecture_example2.all_addresses(), [
    [],
        ['a'],
            ['a', 'a'],
            ['a', 'b'],
                ['a', 'b', 'a'],
                ['a', 'b', 'b'],
        ['b'],
            ['b', 'a'],
                ['b', 'a', 'a'],
                ['b', 'a', 'b'],
            ['b', 'b']
])

print('Wszystkie testy zaliczone!')

