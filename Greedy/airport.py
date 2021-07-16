g = int(input())
p = int(input())

ap = []

for _ in range(p):
    ap.append(int(input()))

def find(x):
    if x == parent[x]:
        return x

    p = find(parent[x])
    
    parent[x] = p
    
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    parent[x] = y

parent = {i:i for i in range(g+1)}

cnt = 0

for i in ap:
    x = find(i)
    print(i,parent)
    if x == 0:
        break

    union(x,x-1)
    cnt += 1
    print(i,parent)


print(cnt)    

