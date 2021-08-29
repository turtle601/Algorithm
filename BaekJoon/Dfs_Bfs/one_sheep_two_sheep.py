from collections import deque

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q.append((i,j))
    visited[i][j] = True

    while q:
        y,x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            
            if graph[ny][nx] == '.':
                continue

            if visited[ny][nx] == False and graph[ny][nx] == '#':
                visited[ny][nx] = True
                q.append((ny,nx))



for  _ in range(n):
    h,w = map(int, input().split())
    
    graph = [list(map(str, input())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0

    q = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#' and visited[i][j] == False:
                
                bfs(i,j)
                count += 1

    print(count)            

