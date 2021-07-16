### 백준 1916번
## 최소비용 구하기
# 그래프(다익스트라 알고리즘)

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

# 그래프 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)

        # 방문 여부 따지기 - 최단 거리가 갱신이 된 상태이므로
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))      

dijkstra(start)

print(distance[end])