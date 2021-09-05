# 백준 1708 볼록껍질
# 플레티넘 5

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1])-(p2[1]-p1[1])*(p3[0]-p2[0]);

def monotoChain():
    upper = []
    lower = []

    points.sort(key = lambda x: (x[0], x[1]))

    for point in points:
        while (len(upper) >= 2 and ccw(upper[-2],upper[-1],point) <= 0):
            upper.pop();  
        while (len(lower) >= 2 and ccw(lower[-2],lower[-1],point) >= 0):
            lower.pop();  

        upper.append(tuple(point))
        lower.append(tuple(point))

    return len(list(set(upper + lower)))

print(monotoChain())    