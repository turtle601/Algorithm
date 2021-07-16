n = int(input())

wei = list(map(int, input().split()))

wei.sort()

result = 1

for i in wei:
    if result < i:
        break

    result += i

print(result)    
