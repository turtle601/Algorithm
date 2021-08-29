from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        for i in graph[x]:
            # 아직 방문하지 않았다아면 
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            
            # 방문했다아면    
            else:
                # 옆에 붙어있는 두 노드가 값이 같다면 False
                if visited[i] == visited[x]:
        
                    return False
    return True                

for _ in range(n):
    v,e = map(int, input().split())
    
    graph = [[] for _ in range(v+1)]

    visited = [0] * (v+1)

    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True

    for i in range(1,v+1):
        
        if visited[i] == 0:
           
            result = bfs(i)
            if not result:
                break
                 
    print("YES" if result else "NO")
