import sys
input = sys.stdin.readline

n = int(input())

rgb = [list(map(int, input().split())) for _ in range(n)]

# r,g,b 각각의 색깔을 선택했을 때 집을 칠할 수 있는 비용이 최솟값을 저장
dp = [[0]*(n+1) for _ in range(3)]

for i in range(1,n+1):
    for j in range(3):

        #빨간색 선택 시
        if j == 0:
            #선택할 수 있는 파랑과 초록 중 최솟값 선택
            dp[j][i] = min(dp[1][i-1],dp[2][i-1]) + rgb[i-1][0] 
        
        #초록색 선택 시
        elif j == 1:
            #선택할 수 있는 빨강과 파랑 중 최솟값 선택
            dp[j][i] = min(dp[0][i-1],dp[2][i-1]) + rgb[i-1][1] 

        #파란색 선택 시        
        else:
            #선택할 수 있는 빨강과 초록 중 최솟값 선택
            dp[j][i] = min(dp[0][i-1],dp[1][i-1]) + rgb[i-1][2] 

result = []

for i in range(3):
    result.append(dp[i][n])    

print(min(result))