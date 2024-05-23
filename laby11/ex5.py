from collections import deque, defaultdict

def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return top_order

def shortest_path(graph, u, v):
    # Wykonaj sortowanie topologiczne DAG
    top_order = topological_sort(graph)

    # Inicjuj odległości
    distance = {node: float('inf') for node in graph}
    distance[u] = 0

    # Relaksacja krawędzi zgodnie z kolejnością topologiczną
    for node in top_order:
        if distance[node] != float('inf'):
            for neighbor, weight in graph[node]:
                if distance[neighbor] > distance[node] + weight:
                    distance[neighbor] = distance[node] + weight

    return distance[v]

graph = {
    'A': [('B', 3), ('C', 6)],
    'B': [('C', 4), ('D', 4), ('E', 11)],
    'C': [('D', 8), ('G', 11)],
    'D': [('E', -4), ('F', 5), ('G', 2)],
    'E': [('H', 9)],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

u = 'A'
v = 'H'
print(f"Najkrótsza ścieżka z {u} do {v} wynosi: {shortest_path(graph, u, v)}")
