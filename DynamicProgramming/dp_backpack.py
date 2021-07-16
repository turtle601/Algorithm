#배낭 무게 동적 계획법

import sys
input = sys.stdin.readline

n,w = map(int,input().split())

lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(1,n+1):
    wei = lst[i-1][1]
    v = lst[i-1][0]

    for j in range(1,w+1):
        if j >= wei:
            dp[i][j] = max(dp[i-1][j-wei]+v, dp[i-1][j])
            
        else:
            dp[i][j] = dp[i-1][j]         
        
print(dp[-1][-1])