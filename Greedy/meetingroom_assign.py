n = int(input())

lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort()

cnt = 0

result = [0,0]

for i in lst:
    if result[1] <= i[0]:
        cnt += 1
        result = [result[0],i[1]]
    elif result[0] <= i[0] and i[1] <= result[1]:
        result = [result[0], i[1]]

print(cnt)

