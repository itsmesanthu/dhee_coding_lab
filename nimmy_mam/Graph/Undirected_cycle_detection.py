#undirected graph cycle detection 
def has_cycle(graph,node,parent,visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
           if  has_cycle(graph,neighbor,node,visited):
            return True
        elif neighbor!=parent:
            return True
    return False
def contains_cycle(graph):
    visited=set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph,node,-1,visited):
                return True
    return False
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(contains_cycle(graph))

graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}

print(contains_cycle(graph))