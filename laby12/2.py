from wyklad11 import Graph, GraphNode


def is_connected(graph: Graph) -> bool:
    if not graph.nodes:
        return True
    start_node = next(iter(graph.nodes.values()))
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited) == len(graph.nodes)

# Testy.
G1 = Graph(
    ['A', 'B', 'C', 'D'],   # lista wierzchołków grafu
    ['AB', 'AC', 'BD', 'DA', 'DC'], # krawędzie
    directed=False
)
assert is_connected(G1) == True

G2 = Graph(
    ['A', 'B', 'C', 'D'],
    ['AB', 'AC', 'BA'],
    directed=False
)
assert is_connected(G2) == False

G3 = Graph(
    ['A', 'B', 'C', 'D'],
    ['AB', 'AC', 'AD', 'BC', 'BD', 'CD'],
    directed=False
)
assert is_connected(G3) == True

G4 = Graph(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    ['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH'],
    directed=False
)
assert is_connected(G4) == True

G5 = Graph(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    ['AB', 'BC', 'CD', 'DB', 'EF', 'FG', 'GH'],
    directed=False
)
assert is_connected(G5) == False

G6 = Graph(
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'EF'],
    directed=False
)
assert is_connected(G6) == False
