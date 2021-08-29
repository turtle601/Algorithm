### 백준 11404 플로이드
## 그래프(플로이드 와샬)
# 모든 도시의 쌍(A,B)에 대해서 도시 A - B로 가는 데 필요한 비용의 최솟값을 구하라

import sys
input = sys.stdin.readline

INF = 100000000

n = int(input())
m = int(input())

# 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 그래프에 비용의 최솟값 삽입 
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)

# 플로이드 와샬을 통해 최단 거리 구하기
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 그래프 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
            
