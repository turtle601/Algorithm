# BaekJoon 11054번
# 가장 긴 바이토닉 부분 수열

# 입력
# 10
# 1 5 2 1 4 3 4 5 2 1

# 출력
# 7

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

up_dp = [1] * n
down_dp = [1] * n

result = 0

# dp 만드는 함수
def make_dp(lst,dp):
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)

# 왼쪽에서 가장 긴 증가수열 찾을 때
make_dp(lst,up_dp)

# 오른쪽에서 부터 가장 긴 증가수열을 찾을 때
make_dp(lst[::-1], down_dp)

for up, down in zip(up_dp, down_dp[::-1]):
    if (up + down) > result:
        result = up + down

print(result-1)

