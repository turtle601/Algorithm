# 백준 2293번 동전 1
# DynamicProgramming(동적 계획법)

import sys
input = sys.stdin.readline

n,k = map(int, input().split())

#dp 리스트 생성
dp = [1] + [0] * k

coins = [int(input()) for _ in range(n)]

for coin in coins:
    for j in range(coin, k+1):
        #해당 코인이 첫번째 코인일 경우 나머지가 0일 경우 1을 집어 넣는다. 
        if coin == coins[0] and j % coin == 0:
            dp[j] = 1
        #해당 코인이 첫번째 코인이 아닐 경우 
        else:
            #원래 dp값과 해당 자릿수에 -coin을 더해 총 가짓수를 구할 수 있다. 
            dp[j] += dp[j-coin]

print(dp[-1])            



    



       
      
