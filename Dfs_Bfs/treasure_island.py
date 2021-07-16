from collections import deque

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(str,input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):

    queue = deque()
    queue.append((y,x))
    visited[y][x] = True

    while queue:
            
        y,x = queue.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #해당 범위를 벗어날 경우 무시 
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            #바다이면 무시
            if graph[ny][nx] == "W":
                continue
            
            #육지이고 방문하지 않았다면
            if graph[ny][nx] == 'L' and visited[ny][nx] == False:
                visited[ny][nx] = True
                cnt[ny][nx] = cnt[y][x] + 1 
                queue.append((ny,nx))
    return 

result = 0

for i in range(n):
    for j in range(m):
                
        if graph[i][j] == 'L':

            #cnt와 visited 초기화
            cnt = [[0]*m for _ in range(n)]          #해당 L지역까지 도달했을때의 최단 거리를 기록
            visited = [[False]*m for _ in range(n)]  #방문했는지 여부를 나타내는 리스트
            bfs(i,j)

            #이차원 배열 중 제일 큰 값들 중 max 값, result
            result = max(result,max(map(max,cnt)))

print(result)
