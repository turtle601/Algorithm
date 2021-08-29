# 백준 - 문자열 폭발

import sys
input = sys.stdin.readline

word = list(input().strip())
boom = list(input().strip())

#boom의 리스트 길이 n
n = len(boom)

result = []

for i in range(len(word)):
    # word에 각 문자 하나하나씩 result에 집어 넣는다. 
    result.append(word[i])

    #만약 result에서 끝에서 n만큼 떨어진 리스트가 boom과 같다면
    if result[-n:] == boom:
        for _ in range(n):
            #result에서 제외 pop
            result.pop()    

#result에 값이 있다면
if result:
    print((''.join(result)))
         
else:
    print('FRULA') 
      