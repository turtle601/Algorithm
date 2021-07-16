### 프로그래머스 스파이
## Level 2
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    
    dic = {}
    answer = 0  

    for clo in clothes:
        if clo[1] not in dic:
            dic[clo[1]] = 1
        else:
            dic[clo[1]] += 1

    mul = 1

    for val in dic.values():
        mul *= (val + 1)

    return mul - 1