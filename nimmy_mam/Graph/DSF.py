#itirative dfs using stack
def DfsUsingStack(graph,start):
    stack=[start]
    visited={start}
    while stack:
        node=stack.pop()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}
DfsUsingStack(graph,0)
print()
print("------------------------")
#Recursive DFS

def DfsUsingRecursive(graph,node,visited):
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DfsUsingRecursive(graph,neighbor,visited)
visited=set()
start=0
DfsUsingRecursive(graph,start,visited)