from collections import deque
# n = 세로, m = 가로
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(str,input())))

visited = [[False]*m for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,1,-1]

sheep = 0
wolf = 0

def bfs(a,b):
    q = deque()
    result = [0,0]  # 울타리 내에 있는 양,늑대의 마리 수 정보를 넣은 리스트

    #처음 방문했을 때 양 또는 늑대가 있을 때
    if graph[a][b] == 'o':
        result[0] += 1
            
    elif graph[a][b] == 'v':
        result[1] += 1

    q.append((a,b))
    visited[a][b] = True
   
    while q:
        y,x = q.popleft()
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[ny][nx] != '#' and visited[ny][nx] == False:
                visited[ny][nx] = True

                #이동 시 양 또는 늑대가 있을 시 
                if graph[ny][nx] == 'o':
                    result[0] += 1

                elif graph[ny][nx] == 'v':
                    result[1] += 1

                q.append((ny,nx))
           
    return result    
                            

for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and visited[i][j] == False:
            
            ans = bfs(i,j)
            
            #전체 양과 늑대의 개수 sheep, wolf 
            if ans[0] > ans[1]:
                sheep += ans[0]

            else:
                wolf += ans[1]
      
print(sheep,end = " ")
print(wolf)

    
