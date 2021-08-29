# 백준
# N-Queen 9663번
# 백트래킹

# 접근 방법 (check 함수) 
# 퀸이 놓여지기 위해서 퀸의 위치의 가로축과 세로축 그리고 대각선은 퀸이 놓일 수 없다. 
# 이때, 한 가로축에 퀸 하나를 배정한다면 그 가로축에는 더 이상 퀸을 생성할 수 없다. 
# ==> 방문 기록을 1차원 배열(visited)로 나타낼 수 있다. 대각선과 세로축만 고려하면 된다.  

# 2차원 배열에서 (1,1) , (2,2) 두 값이 대각선 위치에 놓여져 있는지 확인하기 위해서
# x좌표 두 값 뺀 값과 y축 좌표 두 값을 뺀 값이 같다면 두 좌표는 대각선에 놓여 있다고 할 수 있다.

import sys
input = sys.stdin.readline

n = int(input())

# visited에 있는 값들은 다 다른 값들이 놓여져야한다. 
visited = [-1] * n

# 결과 값
count = 0

def check(depth):
    
    #비숍을 놓을 수 있으면 True 아니면 False
    for i in range(depth):
        if visited[depth] == visited[i] or abs(visited[depth] - visited[i]) == depth - i:
            return False

    return True        

def dfs(depth):
    global count
    
    # 만약 모든 깊이를 다 탐색했다면 횟수 += 1
    if depth == n:
        count += 1
        return     

    for i in range(n):
        
        visited[depth] = i

        if check(depth):
            dfs(depth + 1)
        

dfs(0)

print(count)


     



        