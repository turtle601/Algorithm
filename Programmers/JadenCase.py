### 프로그래머스 JadenCase 문자열 만들기
## Level 2
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/12951#

## 입력값
# 1. "3people unFollowed me"
# 2. "for the last week"

def solution(s):
    up = True
    result = []
    
    for i in range(len(s)):
        if up:
            if s[i].isalpha():
                result.append(s[i].upper())
                up = False
            else:
                if s[i] == " ":
                    up = True
                else:
                    up = False
                
                result.append(s[i])
                   
        else:
            if s[i].isalpha():
                result.append(s[i].lower())
                
            else:
                if s[i] == " ":
                    up = True
                
                result.append(s[i])
                
    return "".join(result)