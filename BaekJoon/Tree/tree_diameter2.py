from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n):
    lst = list(map(int, input().split()))
    
    i = 1
    while lst[i] != -1:
        graph[lst[0]].append(lst[i:i+2])
        i += 2 

visited = [False] * (n+1)
cnt = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not visited[i[0]]:
                visited[i[0]] = True
                cnt[i[0]] = cnt[x] + i[1]
                q.append(i[0])

    return max(cnt)

k = bfs(1)
idx = cnt.index(k)

visited = [False] * (n+1)
cnt = [0] * (n+1)

result = bfs(idx)
print(result)
