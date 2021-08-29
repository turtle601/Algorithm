n,m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 깊이를 나타내는 count == 4인 것을 나타내기 위한 전역 변수
check = [0] 

def dfs(graph,v,visited,count):
    
    visited[v] = True
    
    if count == 4:
        check[0] = 1 
        return 
    
    for i in graph[v]:

        if visited[i] == False:
            dfs(graph,i,visited,count+1)
            #노드의 다른 길 방문을 위해 리셋
            visited[i] = False 

result = 0

visited = [False] * n

for i in range(n):
    #방문기록을 나타내는 visited 리셋
    visited[i] = [False]
    dfs(graph,i,visited,0)
    
    if check[0] == 1:
        result = 1
        
        break

if result == 1:
    print(1)
else:
    print(0)    
