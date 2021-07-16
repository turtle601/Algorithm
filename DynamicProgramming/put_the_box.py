# 백준 1965번
# 상자 넣기
# 동적계획법

#원래 나의 풀이
import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

dp = [1] * len(lst)

for i in range(1,len(lst)):
    check = []
    # 해당 노드의 주소보다 주소값이 작은 것들 중
    for j in range(i-1,-1,-1):
        # 해당 노드의 값보다 작은 값들의 dp값들을 모두 check리스트에 넣는다. 
        if lst[i] > lst[j]:
            check.append(dp[j])
            # 그 값들 중 최대값 + 1 해준다.  
            dp[i] = max(check) + 1


print(max(dp))

# 다른 사람들의 풀이

# import sys, bisect

# input = sys.stdin.readline

# n = int(input())
# boxes = map(int, input().split())
# memoization = [0]

# for box in boxes:
      # 마지막 값이 box보다 작다면 추가
#     if memoization[-1] < box:
#         memoization.append(box)
      
      # 마지막 값이 box보다 크다면 
#     else:
          # 해당 값 box를 이분탐색하여 위치할 자리를 찾아 준다. (오름차순으로 정렬이 될 - 왼쪽부터)   
#         index = bisect.bisect_left(memoization, box)
          # 해당 index 위치를 box값으로 바꿔준다. 
#         memoization[index] = box

# print(len(memoization) - 1)