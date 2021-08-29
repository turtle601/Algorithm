n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]

for i in range(1,n):            # i는 간격에 따른 대각선 줄을 의미한다.  
    for j in range(n-i):        # j는 대각선의 항목들
        x = i + j
        dp[j][x] = 2 ** 32

        for k in range(j,x):   # 나올 수 있는 모든 최솟값을 구한다. 
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + graph[j][0] * graph[k][1] * graph[x][1])

print(dp[0][n-1])
                         
