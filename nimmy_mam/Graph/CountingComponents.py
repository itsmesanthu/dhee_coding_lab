def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
def count_components(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1

    return count
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

print(count_components(graph))