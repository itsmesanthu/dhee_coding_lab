'''def happy(n):
    if n==1:
        return True
    elif n==4:
        return False
    sum=0
    while n>0:
        base=n%10
        sum=sum+(base*base)
        n=n//10
    return happy(sum)
n=int(input("enter the number : "))
flag=happy(n)
if flag:
    print("happy number")
else:
    print("unhappy number")'''

def bfs(graph, visited, start):

    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)


# Graph representation using dictionary
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours separated by space: ").split()
    graph[node] = neighbours

visited = set()

start = input("Enter starting node: ")

if start not in graph:
    print("Starting node not present in graph")
else:
    print("DFS Traversal:")
    bfs(graph, visited, start)