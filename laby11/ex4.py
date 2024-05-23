from collections import deque, defaultdict


def topological_sort_kahn(graph):
    # Oblicz stopnie wejściowe każdego wierzchołka
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Kolejka dla wierzchołków o stopniu wejściowym 0
    queue = deque([u for u in graph if in_degree[u] == 0])
    top_order = []  # Lista dla przechowywania porządku topologicznego

    # Proces sortowania
    while queue:
        vertex = queue.popleft()
        top_order.append(vertex)
        # Przejście przez wszystkich następców danego wierzchołka
        for neighbour in graph[vertex]:
            in_degree[neighbour] -= 1  # Zmniejszenie stopnia wejściowego
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    # Sprawdzenie, czy wszystkie wierzchołki zostały przetworzone
    if len(top_order) != len(graph):
        return None  # Istnieje cykl, co jest niemożliwe dla DAG
    return top_order


# Przykładowe użycie
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
print(topological_sort_kahn(graph))
