n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

sum = 0

flag = lst[-1]

for i in range(len(lst)-2,-1,-1):
    flag -= 1

    if lst[i] > flag:
        sum += lst[i] - flag
        
    else:
        flag = lst[i]   

print(sum)        
