from wyklad11 import Graph, GraphNode

def bfs(graph: Graph, start: GraphNode):
    nodes_in_dist = [[start]]
    # nodes_in_dist[d] - lista wierzchołków w odległości d od wierzchołka startowego.
    # Stan początkowy: nodes_in_dist[0] == [start]
    size = len(graph.nodes)
    processed = {start} # Zbiór wierzchołków, których odległość od wierzchołka startowego już znamy.
    for d in range(size):
        # nodes_in_dist[d] już jest obliczone; konstruujemy nodes_in_dist[d+1].
        nodes_in_dist.append([])
        for node in nodes_in_dist[d]:
            for successor in node.neighbors:
                if successor not in processed:
                    nodes_in_dist[d+1].append(successor)
                    processed.add(successor)
    return nodes_in_dist

G = Graph(
    ['A', 'B', 'C', 'D'],   # lista wierzchołków grafu
    ['AB', 'AC', 'BD', 'DA', 'DC'], # krawędzie
    directed=True   # jeśli ustawione na False, wszystkie krawędzie stają się dwustronne
)
print('Graf:')
G.PrintEdges()
nodes_in_dist = bfs(G, G.nodes['A'])
print('Wierzchołki w danej odległości od A:')
for d in range(len(nodes_in_dist)):
    nodes = [node.id for node in nodes_in_dist[d]]
    print(f'\tw odległości {d}: {nodes}')
