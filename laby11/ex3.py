def count_paths(graph, u, v, memo):
    if u == v:
        return 1
    if u in memo:
        return memo[u]

    total_paths = 0
    for neighbor in graph.get(u, []):
        total_paths += count_paths(graph, neighbor, v, memo)

    memo[u] = total_paths
    return total_paths

def main():
    # Przykładowy graf w formie listy sąsiedztwa
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }

    u = 'A'
    v = 'E'
    memo = {}
    result = count_paths(graph, u, v, memo)
    print(f"Liczba różnych ścieżek z {u} do {v} wynosi: {result}")

main()
