import heapq

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

start = input("Enter start node: ")

visited = []
heap = []

heapq.heappush(heap, start)
visited.append(start)

while heap:
    curr = heapq.heappop(heap)
    print(curr, end=" ")

    for nb in graph[curr]:
        if nb not in visited:
            visited.append(nb)
            heapq.heappush(heap, nb)

print("\nTraversal done")
# Sample input:
# Enter number of nodes: 3
# Enter node name: A
# Enter neighbors separated by space: B C
# Enter node name: B
# Enter neighbors separated by space: A
# Enter node name: C
# Enter neighbors separated by space: A
# Enter start node: A

# Output:
# A B C
# Traversal done