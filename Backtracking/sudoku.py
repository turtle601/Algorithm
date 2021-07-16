import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == 81:
        for ans in graph:
            print("".join(map(str, ans)))
        # 사전 식으로 앞서는 것을 출력해야 하기 때문에 하나만 출력하고 exit() 한다. 
        exit()
        return

    row = depth // 9
    col = depth % 9
  
    if graph[row][col] == 0:
        for i in range(1,10):
            # 만약 i값에 가로축, 세로축, 3X3 정사각형에 겹치는 게 없다면(모두 다 False) 
            if not row_visited[row][i] and not col_visited[col][i] and not three_box[3 * (row // 3) + (col // 3)][i]:
                row_visited[row][i] = col_visited[col][i] = three_box[3 * (row // 3) + col // 3][i] = True
                graph[row][col] = i

                dfs(depth + 1) # 1 ~ 9 중 들어갈 수가 없다면 리턴
                
                # 다시 원래 값으로 돌려줘야 한다.  
                row_visited[row][i] = col_visited[col][i] = three_box[3 * (row // 3) + (col // 3)][i] = False
                graph[row][col] = 0

    else:
        dfs(depth + 1)


graph = [list(map(int, input().strip())) for _ in range(9)]

row_visited = [[False] * 10 for _ in range(9)] # 가로축에 1,2,3,4,5,6,7,8,9가 있는지 확인
col_visited = [[False] * 10 for _ in range(9)] # 세로축에 1,2,3,4,5,6,7,8,9가 있는지 확인
three_box = [[False] * 10 for _ in range(9)]   # 3 X 3에 1,2,3,4,5,6,7,8,9가 있는지 확인 (왼쪽 위 정사각형을 0,...)

result = []

# graph에서 0이 아닌 숫자에 대해 미리 입력(row_visited, col_visited, three_box)
for i in range(9):
    for j in range(9):
        if graph[i][j] != 0:
            row_visited[i][graph[i][j]] = True
            col_visited[j][graph[i][j]] = True
            three_box[3 * (i // 3) + (j // 3)][graph[i][j]] = True

dfs(0)
