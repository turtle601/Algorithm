n, money = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))

flag = 0   # flag = 0 사야할 때, flag = 1 팔아야 할 때
coin = 0

for i in range(n-1):
    if lst[i] < lst[i+1] and flag == 0:
        coin = money // lst[i]
        money %= lst[i]
        flag = 1
    
    if lst[i] > lst[i+1] and flag == 1:
        
        money += coin * lst[i]
        coin = 0
        flag = 0

if coin != 0:
    money += coin * lst[-1]

print(money)        
