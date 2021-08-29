n = int(input())

for _ in range(n):
    k = int(input())
    lst = list(map(int, input().split()))
    
    sum = 0
    hi = 0

    for i in range(len(lst)-1,-1,-1):
        if hi >= lst[i]:
            sum += hi - lst[i]
        else:
            hi = lst[i]

    print(sum)                    
