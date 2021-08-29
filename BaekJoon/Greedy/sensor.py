n = int(input())

k = int(input())

sens = list(map(int, input().split()))

if n <= k:
    print(0)

else:    
    sens.sort()

    distance = []

    for i in range(1,n):
        distance.append(sens[i] - sens[i-1])

    distance.sort()

    for _ in range(1,k):
        distance.pop()

    print(sum(distance))


