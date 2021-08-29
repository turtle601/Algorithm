#PPAP
import sys
input = sys.stdin.readline

word = input().strip()

#시간복잡도를 줄이기 위해 문자열을 리스트로 하나씩 입력받는다. 
stack = []

for i in range(0,len(word)):
    stack.append(word[i])

    #만약 마지막 4단어가 PPAP일 경우 맨 앞 P를 제외한 나머지 단어들을 제외(pop)시킨다. 
    if stack[-4:] == ['P','P','A','P']:
        stack.pop()
        stack.pop()
        stack.pop()

if stack == ['P'] or stack == ['P','P','A','P']:
    print('PPAP')

else:
    print('NP')    
