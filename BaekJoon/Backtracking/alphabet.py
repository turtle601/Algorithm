### 백준 
## 알파벳 1987번
# 백트래킹
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

result = 0

alpha = [0] * 26
alpha[ord(graph[0][0]) - 65] = 1

def dfs(y,x,depth):
    global result
    result = max(result,depth)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and alpha[ord(graph[ny][nx]) - 65] == 0:
            alpha[ord(graph[ny][nx]) - 65] = 1
            dfs(ny,nx,depth+1)
            alpha[ord(graph[ny][nx]) - 65] = 0

dfs(0,0,1)
print(result)

