import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
# 내림차순 정렬
lst.sort(reverse=True)

# 가장 높은 레벨
choice = lst[0]

sum = 0

for i in range(1,n):
    # 가장 높은 레벨과 합성
    sum += (choice + lst[i])

print(sum)    
