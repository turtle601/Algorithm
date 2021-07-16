import sys
input = sys.stdin.readline

n,m=map(int, input().split())

graph = []

#가장 작은 hamming Distance DNA
ans = ''

#가장 작은 hamming Distance 답
result = 0 

for _ in range(n):
    
    graph.append(list(input()))

for i in range(m):
    # 각 문자열의 자릿수에서 알파벳 별로 나온 횟수를 체크하여
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for j in range(n):
        dic[graph[j][i]] += 1

    val = list(dic.values())
    m = max(val)
    
    # 가장 많이 나온 알파벳(m)은 hamming Distance가 가장 작은 DNA(ans)를 형성
    if dic['A'] == m:
        ans += 'A'
    elif dic['C'] == m:
        ans += 'C'
    elif dic['G'] == m:
        ans += 'G'
    elif dic['T'] == m:            
        ans += 'T'
    
    # 나머지 횟수들은 ans와 다른 알파벳이므로
    # hamming Distance의 합(result)에 대해주었다. 
    result += (sum(val) - m)

print(ans)
print(result)