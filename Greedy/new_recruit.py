import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    
    lst = []

    for _ in range(n):
        lst.append(list(map(int, input().split()))) 

    lst.sort()

    for i in range(len(lst)):
        if i == 0:
            m = lst[i][1]
            sum = 1
        else:
            if lst[i][1] < m:
                sum += 1
                m = lst[i][1]
    print(sum)