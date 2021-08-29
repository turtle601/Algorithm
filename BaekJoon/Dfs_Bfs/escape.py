#알고리즘 설명:
#물의 이동을 bfs, 비버의 이동을 bfs로 구현한다. 
#이때 물을 먼저 이동시키고 물 방문 여부를 확인한 후 비버를 이동시킨다. (물 한 칸, 비버 한 칸)

from collections import deque
n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(str, input())))

visited1 = [[False]*m for _ in range(n)] #물 방문 확인 리스트
visited2 = [[False]*m for _ in range(n)] #비버 방문 확인 리스트

biber = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*': #물
            queue.appendleft((i,j,1)) #물을 먼저 구현하기 위해
            visited1[i][j] = True
        if graph[i][j] == 'S': #비버
            queue.append((i,j,0))
            visited2[i][j] = True
        if graph[i][j] == 'D': #도착지점
            search = [i,j]

def bfs():
    
    while queue:
        y, x, z= queue.popleft() #y,z는 좌표 z는 물/비버 구별 변수
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            if graph[ny][nx] == 'X': #돌은 무시하자
                continue
            
            #물일 경우
            if (graph[ny][nx] == '.' or graph[ny][nx] == 'S') and visited1[ny][nx] == False and z == 1:
                visited1[ny][nx] = True
                queue.append((ny,nx,z))
           
            #비버일 경우
            elif (graph[ny][nx] == 'D' or graph[ny][nx] == '.') and visited1[ny][nx] == False and visited2[ny][nx] == False and z == 0:
                biber[ny][nx] = biber[y][x] + 1
                visited2[ny][nx] = True
                queue.append((ny,nx,z))

    return biber[search[0]][search[1]] # 비버 도착지점 리턴


if bfs() == 0:
    print("KAKTUS")

else:
    print(bfs())    

