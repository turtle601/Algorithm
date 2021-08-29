import heapq

import sys

input = sys.stdin.readline

INF = int(1e9)
# 노드의 개수, 간선의 개수
n,m = map(int, input().split())

# 시작점
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 다익스트라 알고리즘(우선순위 큐 자료구조 이용)
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(최단거리가 이미 표시 되어 있으므로)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

# 거리정보를 나타내는 distance 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])