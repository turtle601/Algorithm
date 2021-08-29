import heapq
n,k = map(int, input().split())

jew = []

bag = []

for _ in range(n):
    jew.append(list(map(int, input().split())))

for _ in range(k):
    bag.append(int(input()))

jew.sort()  # 보석 무게 오름차순 정렬 
bag.sort()  # 가방 한도 무게 오름차순 정렬

j = 0

queue = []

result = 0

for i in range(k):
    while j < n:
        #보석의 무게가 가방 한도보다 작다면
        if jew[j][0] <= bag[i]:
            heapq.heappush(queue, -jew[j][1]) #최대값만 빼내기 위해 -1을 곱한다.
            j += 1
        #보석의 무게가 가방 한도보다 크다면 <while문 탈출>
        else: 
            break
    
    if queue:
        result += (-1) * heapq.heappop(queue) #원래의 값을 도출하기 위해 다시 -1을 곱한다.

print(result)



