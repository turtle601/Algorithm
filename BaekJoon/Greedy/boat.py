import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int, input().split()))
m = int(input())
b_wei = list(map(int, input().split()))

#크레인의 무게한도(limit)와 박스의 무게(b_wei)를 내림차순으로 정렬
limit.sort(reverse=True)
b_wei.sort(reverse=True)

ans = 0

# 크레인의 무게한도의 최댓갑보다 큰 박스 무게가 있을 시 박스를 운송할 수 없다. 
if limit[0] < b_wei[0]:
    print(-1)
    exit()    

#각 무게 한도 보다 작은 박스가 있다면 b_wei리스트에서 하나씩 없앤다. 
while len(b_wei) > 0:
       
    for i in limit:
        for j in range(len(b_wei)):
            if i >= b_wei[j]:
                del b_wei[j] 
                break
    # 각 무게 한도 사이클을 다 돌았으면 ans += 1
    ans += 1
print(ans)    