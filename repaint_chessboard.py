n,m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(str, input())))

result1 = 0
result2 = 0

for i in range(n):
    
    for j in range(m):
        if board[i][j] == 'W':
            board[i][j] = 1
        
        if board[i][j] == 'B':
            board[i][j] = 0

graph1 = [[0]*50 for _ in range(50)] 
graph2 = [[0]*50 for _ in range(50)]

for i in range(50):
    
    for j in range(50):
        
        graph1[i][j] = (i+j) % 2  #graph1은 블랙부터 시작하는 체스판
        graph2[i][j] = (i +j + 1) % 2 #graph2는 화이트 부터 시작하는 체스판

a = m*n

for i in range(n-7):
    for j in range(m-7):  #8X8 체스판을 이동시키는 구문
        result1 = 0
        result2 = 0
        for p in range(i,i+8): #작은 체스판에서 기존의 체스판(graph1과 graph2)와 일치하는 지 확인
            for q in range(j,j+8):
               
                if graph1[p][q] != board[p][q]:
                    result1 +=1

                if graph2[p][q] != board[p][q]:
                    result2 +=1    
                
        a = min(a,result1,result2)

print(a)

         
        


        




