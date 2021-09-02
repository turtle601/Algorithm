# 백준 14501번
# 퇴사

import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for i in range(n+1)]

# 날짜를 거꾸로 순회
for i in range(n-1,-1,-1):
    # 기한이 지났다면 dp 그 전 값을 복사
    if i + lst[i][0] > n:
        dp[i] = dp[i+1]

    # 그렇지 않다면 연결된 구간에서의 합 or 기존의 최댓값과 비교하여 dp에 저장
    else:
        dp[i] = max(lst[i][1] + dp[i + lst[i][0]],dp[i+1])    

# 출력
print(dp[0])