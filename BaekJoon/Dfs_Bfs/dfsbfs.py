from collections import deque

# 정점의 개수 n, 간선의 개수 m,  시작할 정점의 번호 l
n,m,l = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 안에 리스트들을 오름 차순으로 정렬
for i in graph:
    i.sort()

visited = [False] * (n+1) # dfs방문여부 판단
visited2 = [False] * (n+1) # bfs 방문여부 판단

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited2):
    queue = deque([start])
    visited2[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if visited2[i] == False:
                queue.append(i)
                visited2[i] = True

dfs(graph,l,visited)                
print()
bfs(graph,l,visited2)
