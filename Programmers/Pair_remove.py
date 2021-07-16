### 프로그래머스 짝지어 제거하기
## Level 2
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):
    
    stack = []
    s = list(s)

    for word in s:
        if len(stack) > 0:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)

    if len(stack) > 0:
        return 0
    else:
        return 1