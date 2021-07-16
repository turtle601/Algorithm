### 프로그래머스 프린터
## Level 2
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

# 입력값
# 1. [2,1,3,2],2
# 2. [1,1,9,1,1,1],5

from collections import deque

def solution(priorities, location):
    prior = deque()
    result = [0] * len(priorities)
    cnt = 1
    
    # prior 큐 리스트에서 가장 큰 value값을 찾는 함수
    def find_max(prior):
        max = 0
        for p in prior:
            if p[1] >= max:
                max = p[1]
        return max
    
    for idx, val in enumerate(priorities):
        prior.append((idx,val))
    
    while len(prior) > 0:
        max = find_max(prior)
        j = prior.popleft()
        
        if j[1] >= max:
            result[j[0]] = cnt
            cnt += 1
        
        else:
            prior.append(j)
            
    return result[location]