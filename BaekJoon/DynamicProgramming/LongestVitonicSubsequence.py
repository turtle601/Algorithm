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

up_dp = []
down_dp = []

max = 0
        
check = [0]

# dp 만드는 함수
def make_dp(lst,dp):
    for val in lst:
        if not val in check:
            if check[-1] >= val: 
                check.pop()

            check.append(val)

        dp.append(len(check)-1)
        
make_dp(lst,up_dp)

# 재사용을 위한 check 변수 초기화
check = [0]
make_dp(lst[::-1],down_dp)

for up, down in zip(up_dp, down_dp[::-1]):
    if (up + down) > max:
        max = up + down

print(max)