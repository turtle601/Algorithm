# 햄버거 분배
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

lst = list(input().strip())

visited = [False] * n

cnt = 0

# k범위 왼쪽 가능 여부 확인 함수
def down_check(i,k):
    j = i - k

    # k 범위 왼쪽 가능하지 않다면
    while j < 0:
        j += 1

    return j

# k범위 오른쪽 가능 여부 확인 함수
def up_check(i,k):
    j = i + k

    # k 범위 오른쪽 가능하지 않다면
    while j > n - 1:
        j -= 1

    return j    


for i in range(n):
    if lst[i] == 'P':
        j = down_check(i,k) 
        
        # k 범위 내에 햄버거가 있는지 확인      
        while j <= up_check(i,k):
            
            if lst[j] == 'H' and visited[j] == False:
                visited[j] = True
                cnt += 1
                break 
            
            j += 1

print(cnt)