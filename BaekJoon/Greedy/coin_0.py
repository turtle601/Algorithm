n,k = map(int, input().split())

lst = []

for i in range(n):
    lst.append(int(input()))

big = lst[::-1] #반대로 정렬(내림차순)

count = 0 


for i in big:
    count += k // i  #몫
    k %= i           #나머지


print(count)
