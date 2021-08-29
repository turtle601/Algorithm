### 백준 11403번
## 경로 찾기
# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

graph = []

# graph: 입력 값
for i in range(n):
    graph.append(list(map(int, input().split())))

matrix = [[] for i in range(n)]    

# matrix: 방향이 있는 그래프
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            matrix[i].append(j)

# bfs를 이용하여 start에서 end로 가는 경로가 있는 지 확인
def bfs(start,end):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        for i in matrix[x]:
            if visited[i] == False:
                if i == end:
                    return True
                visited[i] = True
                q.append(i)

    return False

# 출력값 
result = [[0]*n for i in range(n)] 

# 모든 좌표에 대해서 i,j에 간선이 있는지 여부 판단
for i in range(n):
    for j in range(n):
        visited = [False] * n
        if bfs(i,j) == True:
            result[i][j] = 1

# 출력
for i in range(n):
    print(*result[i])    