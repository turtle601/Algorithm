from collections import deque
n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

cnt = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

queue = deque()
queue.append((0,0,0))
visited[0][0] = True

def bfs():
  
    while queue:
        y, x, z = queue.popleft()

        if y == n-1 and x == m-1:
            return cnt[n-1][m-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if graph[ny][nx] == 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                cnt[ny][nx] = cnt[y][x] + 1
                queue.appendleft((ny,nx,z))

            elif graph[ny][nx] == 1 and z == 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                cnt[ny][nx] = cnt[y][x] + 1
                z = 1
                queue.append((ny,nx,z))

    return -1

bfs()
print(bfs())
