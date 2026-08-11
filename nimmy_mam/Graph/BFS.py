from collections import deque
def bfs(graph,start):
    queue=deque([start])
    visited={start}
    while queue:
        node=queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

bfs(graph, 0)
