import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dic = {input().strip() : 0 for _ in range(n)}

result = []

for _ in range(m):
    k = input().strip()
    # dic에서 key값을 찾는 것은 시간 복잡도 O(1)
    if k in dic:
        result.append(k)  

result.sort()

print(len(result))

for i in result:
    print(i)

