# 백준 4181번 ConvexHull
# 플레티넘 5

import sys
input = sys.stdin.readline

n = int(input())

points = []

for _ in range(n):
    x,y,c = map(str,input().split())
    if c == "N": continue
    points.append((int(x),int(y)))

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1])-(p2[1]-p1[1])*(p3[0]-p2[0]);

def convex_hull():
    points.sort()

    upper = []
    lower = []

    for point in points:
        while (len(upper) >= 2 and ccw(upper[-2], upper[-1], point) < 0):
            upper.pop()

        upper.append(point)    

    for point in reversed(points):
        while (len(lower) >= 2 and ccw(lower[-2], lower[-1], point) < 0):
            lower.pop()

        lower.append(point)    

    return upper + lower[1:-1]

result = convex_hull()

# 출력
print(len(result))
for a,b in result:
    print(f'{a} {b}')