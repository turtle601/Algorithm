n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(str, input().split())))

p = [0,0]

def quad(y0,x0,y1,x1,n):
    if n == 1:
        return graph[y0][x0]

    a = n // 2

    r1 = quad(y0,x0,y1+a,x1+a,a)
    r2 = quad(y0,x0+a,y1-a,x1,a)
    r3 = quad(y0+a,x0,y1,x1-a,a)
    r4 = quad(y0+a,x0+a,x1,y1,a)

    if r1 == r2 == r3 == r4 and len(r1) == 1:
        return r1

    for i in [r1,r2,r3,r4]:
        if i == '0':
            p[0] += 1

        elif i == '1':
            p[1] += 1

    return p           

quad(0,0,n,n,n)

print(p[0])
print(p[1])    
