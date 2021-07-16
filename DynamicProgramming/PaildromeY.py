### 백준
## 펠린드롬? 10942번
# Dynamic Programming

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n-i):
        # 펠린드롬의 문자열의 길이 == 1
        if i == 0:
            dp[j][j] = 1

        # 펠린드롬의 문자열의 길이 == 2
        elif i == 1:
            if lst[j] == lst[j+1]:
                dp[j][j+1] = 1

        # 펠린드롬의 문자열의 길이 >= 3
        else:  
            
            # 처음과 끝의 문자가 같고 처음과 끝을 제외한 문자열이 펠린드롬일 때
            if lst[j] == lst[i+j] and dp[j+1][i+j-1] == 1:
                dp[j][i+j] = 1

t = int(input())

for i in range(t):
    s,e = map(int, input().split())
    print(dp[s-1][e-1])