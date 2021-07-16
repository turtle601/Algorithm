from collections import deque

n,m = map(int,input().split())

graph = []

# 위의 문제는 벽을 최대한 덜 뿌시고 미로를 탈출해야 한다. 
# 기존의 미로 탐색으로 최단거리를 구했을 때처럼(bfs로) 구현할 경우 도달할 수 있는 방법이 여러 개 있을 수 있어 어려움이 있다.
# 위의 문제는 이동을 할 경우 0으로 우선으로 이동해야 한다.   
# 따라서, 0을 우선순위로 queue에 집어 넣어(queueleft 사용) 우선적으로 이동 
# 벽을 만날 경우를 나중으로 queue에 집어 넣어(queue 사용) 이동
for i in range(m):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 벽을 최소 몇 번 뿌셧는지 확인하는 리스트
wall_check = [[0] * n for _ in range(m)] 

# 방문했는지 확인하는 리스트
visited = [[False] * n for _ in range(m)]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            
            ny = y + dy[i]
            nx = x + dx[i]
            
            #이동한 벽이 해당 범위에 있을 때
            if 0 <= ny < m and 0 <= nx < n: 

                #벽이고 방문을 아직 안했을 때                
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    wall_check[ny][nx] = wall_check[y][x] + 1
                    visited[ny][nx] = True
                    queue.append([ny,nx]) # 후순위 배치

                #벽이 아니고 방문을 하지 않았을 때 
                elif graph[ny][nx] == 0 and visited[ny][nx] == False:
                    wall_check[ny][nx] = wall_check[y][x]
                    visited[ny][nx] = True
                    queue.appendleft([ny,nx]) #우선순위 배치

    return wall_check[m-1][n-1]

print(bfs(0,0))




    
