from collections import deque

n,m = map(int, input().split())

graph = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    
    #바이러스 방문 확인 리스트(bfs 호출 될 때마다 reset)
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            #바이러스면 queue에 넣어 번지게 함
            if graph[i][j] == 2:
                visited[i][j] = True
                queue.append((i,j))


    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 해당 graph 범위 밖일 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            #         < 바이러스 근처 노드들이 만약>
            if graph[ny][nx] == 1:
                continue
        
            if graph[ny][nx] == 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                
                queue.append((ny,nx))         

    count = 0
    
    # 0의 최대 개수를 구하기 위한 
    for i in range(n):
        for j in range(m):
            # 바이러스 전염구역이 아니고 해당 그래프가 0이 아닌 지역일 경우
            if graph[i][j] == 0 and visited[i][j] == False:
                count += 1

    result[0] = max(result[0],count)            

def wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m): # 노드들을 하나씩 방문
            if graph[i][j] == 0: 
                graph[i][j] = 1
                wall(count+1)  
                graph[i][j] = 0 #만약 탈출조건(count = 3)을 만족한다면 bfs() 호출 후 해당 노드는 방문 취소 

queue = deque()

result = [0]

wall(0)

print(result[0])

