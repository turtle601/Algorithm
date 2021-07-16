### 백준
## 비숍 1799번
# 백트래킹

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 비숍이 갈 수 있는 방향 : / = row + col
slash = [False] * (2*n - 1)

# 비숍이 갈 수 있는 방향 : \ = row - col + n - 1
backSlash = [False] * (2*n - 1)

# color[0]은 black, color[1]은 white를 뜻한다. 
color = [0,0]

# 한 칸씩 모든 노드를 방문하게 되면 시간복잡도가 커져 흑과 백으로 나누어 탐색하였다. 
def dfs(depth,row,col,b_w):
    # col을 두 칸씩 이동시켜 같은 색의 체스판만 이동하게 한다. 
    if col >= n:
        row += 1
        if col % 2 == 0: col = 1
        else: col = 0

    if row == n:
        # depth는 서로가 잡을 수 없는 위치에 비숍을 놓은 개수
        color[b_w] = max(color[b_w],depth)
        return
    
    # 특정 색깔에 대한 모든 경우의 수를 다 따져본다. (최대 몇 개까지 올 수 있는지)
    if graph[row][col] == 1 and not slash[row + col] and not backSlash[row - col + n - 1]:
        slash[row + col] = backSlash[row-col+n-1] = True
        dfs(depth+1,row,col+2,b_w)
        slash[row + col] = backSlash[row-col+n-1] = False
    
    # 해당 조건을 만족 못하거나 or 해당 조건 만족 후 리턴했을 경우 depth 추가 X, col은 두 칸씩 계속 이동
    dfs(depth,row,col+2,b_w)

# black
dfs(0,0,0,0)

# white
dfs(0,0,1,1)

# black + white
print(color[0] + color[1])

    
    


