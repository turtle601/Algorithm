n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(str, input())))

def check(y0,x0,y1,x1,n):
    # 수열의 길이가 1일 경우 종료
    if n == 1:
        return graph[y0][x0]

    # 병합
    a = n // 2

    r1 = check(y0,x0,y1+a,x1+a,a) #왼쪽 위
    r2 = check(y0,x0+a,y1-a,x1,a) #오른쪽 위
    r3 = check(y0+a,x0,y1,x1-a,a) #왼쪽 아래
    r4 = check(y0+a,x0+a,x1,y1,a) #오른쪽 아래

    # 해당 트리의 가지들을 삭제시킨다. 
    if r1 == r2 == r3 == r4 and len(r1) == 1:
        
        return r1

    return "(" +r1+r2+r3+r4 + ")"

print(check(0,0,n,n,n))        

