
import heapq

n = int(input())

graph = []
for _ in range(n):
    dead, cup = map(int, input().split())
    graph.append((dead, cup))

graph.sort()

queue = []

for i in graph:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))

