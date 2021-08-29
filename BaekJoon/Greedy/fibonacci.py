n = int(input())

fib = [0,1]
for i in range(44):
    fib.append(fib[i]+fib[i+1])

fib.sort(reverse=True) # 반대로 뒤집기

def check(k):
    result = []
    for i in fib[0:-2]:
        if i <= k:         # 작은 값이 나오면 result 리스트에 넣는다.
            result.append(i)
            k -= i         
    
    return result

for _ in range(n):
    
    x = int(input())
    ans = check(x)
    ans.sort()
    
    print(*ans) # 리스트를 출력 가능(띄어쓰기 한 채로) 


