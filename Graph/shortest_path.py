### 백준 1753 최단경로
## [최단경로] 다익스트라 알고리즘
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 

import sys
input = sys.stdin.readline

INF = int(1e9)

n,m = map(int, input().split())

# 시작점
start = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append(((v,w)))

# 각 노드의 방문 여부를 따지는 리스트
visited = [False] * (n+1)

# 시작점에서 각 노드에 대한 최단경로를 저장하는 리스트
distance = [INF] * (n+1)

# distance 배열 중 최단 경로가 index 찾기
def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 시작점을 0으로 표시 - 나머지는 모두 INF
    distance[start] = 0
    visited[start] = True

    # 두 정점 사이 여러 간선 중 최솟값만
    for v_w in graph[start]:
        distance[v_w[0]] = min(distance[v_w[0]],v_w[1])

    
    for i in range(n-1):
        
        # distance 배열 중 가장 작은 노드를 찾기
        smallest_node = get_smallest_node()
        visited[smallest_node] = True

        # (경유점 개념) 해당 노드와 연결된 노드들 중 최단 거리를 구한다. 
        for j in graph[smallest_node]:
            cost = distance[smallest_node] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])    

