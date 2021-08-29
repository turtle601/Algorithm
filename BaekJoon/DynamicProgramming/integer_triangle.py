import sys
input = sys.stdin.readline

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

# triangle의 특정 노드 도착 시 걸린 거리의 합을 저장 
dp = [[0] * i for i in range(1,n+1)]

dp[0] = triangle[0]

for i in range(1,n):

    for j in range(len(triangle[i])):
        
        #삼각형의 맨 아래 왼쪽
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]

        #삼각형의 맨 아래 오른쪽
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]

        #삼각형의 맨 아래 중간들은 부모들의 값 비교가 필요(큰 것만 골라 저장)
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])    

print(max(dp[-1]))
