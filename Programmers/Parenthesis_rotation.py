### 프로그래머스 괄호 회전하기
## Level 2
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/76502

# 입력값
# 1: "[](){}" return 3
# 2: "}]()[{" return 2
# 3: "[)(]"   return 0
# 4: "}}}"    return 0

def solution(s):

    answer = 0

    s = list(s)

    dic = {']':'[','}':'{',')':'('}

    # 올바른 괄호 문자열인지 체크
    def check(s):
        stack = []
        for word in s:
            if len(stack) > 0:
                if word not in dic.keys():
                    stack.append(word)
                else:
                    if stack[-1] == dic[word]:
                        stack.pop()
            else:
                stack.append(word)

        if len(stack) == 0:
            return True
        else:
            return False

    # 회전
    cnt = 0
    while cnt < len(s):

        if cnt > 0:
            s += s.pop(0)

        if check(s) == True:
            answer += 1

        check(s)
        cnt += 1

    return answer