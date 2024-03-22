from typing import Union


class Leaf:
    def count_leaves(self):
        return 1

class RegBinNode:
    left: Union['RegBinNode', Leaf]
    right: Union['RegBinNode', Leaf]

    def __init__(self, left: Union['RegBinNode',Leaf], right: Union['RegBinNode',Leaf]):
        self.left = left
        self.right = right
    def count_leaves(self):
        return self.left.count_leaves() + self.right.count_leaves()
    

class RegBinTree:
    root: RegBinNode|Leaf|None
    def __init__(self, node: RegBinNode|Leaf|None = None):
        self.root = node
    
    def count_leaves(self) -> int:
        if self.root is None:
            return 0
        return self.root.count_leaves()


# Testowanie.

tree1 = RegBinTree()
assert tree1.count_leaves() == 0

# Test 2: Drzewo z jednym liściem
leaf1 = Leaf()
tree2 = RegBinTree(leaf1)
assert tree2.count_leaves() == 1

# Test 3: Drzewo z dwoma liśćmi
leaf2 = Leaf()
node1 = RegBinNode(left=leaf1, right=leaf2)
tree3 = RegBinTree(node1)
assert tree3.count_leaves() == 2

# Test 4: Drzewo z trzema liśćmi
leaf3 = Leaf()
node2 = RegBinNode(left=node1, right=leaf3)
tree4 = RegBinTree(node2)
assert tree4.count_leaves() == 3

# Test 5: Drzewo z pięcioma liśćmi na różnych
leaf4 = Leaf()
leaf5 = Leaf()
node4 = RegBinNode(left=node2, right=leaf4)
node5 = RegBinNode(left=node4, right=leaf5)
tree5 = RegBinTree(node5)
assert tree5.count_leaves() == 5

# Test 6: Drzewo z sześcioma liśćmi na różnych poziomach
leaf6 = Leaf()
leaf7 = Leaf()
node6 = RegBinNode(left=leaf6, right=leaf7)
node7 = RegBinNode(left=node5, right=node6)
tree6 = RegBinTree(node7)
assert tree6.count_leaves() == 7

print('Wszystkie testy zaliczone!')
