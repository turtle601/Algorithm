n = int(input())

lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort()

# 과제를 선택해서 높은 배점에 문제만 골라야 할 때 0
flag = 0

result = []

for i in lst:
    flag = i[0] - len(result)
    
    if flag != 0:
        result.append(i[1]) 
        
    #과제를 선택해 높은 배점에 문제만 골라야 할 때
    else:
        # 만약 높은 배점에 문제라면 제일 작은 배점 문제 제외시킨다. 
        result.sort(reverse=True)
        
        if result[-1] < i[1]:
            result.pop()
            result.append(i[1])

print(sum(result))            
