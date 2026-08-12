def contains_cycle(graph):
    visited=set()
    path=set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph,node,visited,path):
                return True
    return False
def has_cycle(graph,node,visited,path):
    visited.add(node)
    path.add(node)
    for neighbor in  graph[node]:
        if neighbor not in visited:
            if has_cycle(graph,neighbor,visited,path):
                return True
        elif neighbor in path:
            return True
    path.remove(node)
    return False
graph = {
    0: [1, 2],
    1: [2],
    2: [ ]
}

print(contains_cycle(graph))
print()
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(contains_cycle(graph))