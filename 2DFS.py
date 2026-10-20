import heapq

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node}: ").split()
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

print("\nDFS traversal done")
# Sample input:
# Enter number of nodes: 3
# Enter node name: A
# Enter neighbors of A: B C
# Enter node name: B
# Enter neighbors of B: A
# Enter node name: C
# Enter neighbors of C: A
# Enter start node: A

# Output:
# A B C
# DFS traversal done
