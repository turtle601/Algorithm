import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 주소값이 1부터 시작하기 위해서
lst = [0] * (n+1)

dic = {}

for i in range(1,n+1):
    a = input().strip()
    # 숫자를 물어봤을 때 바로 대답할 수 있는 lst
    lst[i] = a
    # 포켓몬을 물어봤을 때 바로 대답할 수 있는 dic
    dic[a] = i

for _ in range(m):
    k = input().strip()
    
    # k가 숫자인지 아닌지 판단
    if k.isnumeric():
        print(lst[int(k)])
        
    else:
        print(dic[k])

