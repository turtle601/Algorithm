n,m = map(int, input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

def mul(M,k):
    # k크기가 1이 될 때까지 분할
    if k == 1:
        for i in range(n):
            for j in range(n):
                M[i][j] = M[i][j] % 1000
        return M
    
    elif k % 2 == 0:
        graph = [[0]*n for _ in range(n)]
        C = mul(M,k // 2)
        # 병합
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    graph[i][j] += C[i][k]*C[k][j]
                graph[i][j] %= 1000
        
        return graph

    
    elif k % 2 == 1:
        graph = [[0]*n for _ in range(n)]
        C = mul(M,k-1)
        #병합
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    graph[i][j] += C[i][k]*M[k][j]

                graph[i][j] %= 1000

        return graph

result = mul(mat,m)

for i in result:
    for j in i:
        print(j,end = " ")
    print()    


