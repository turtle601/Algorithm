# 문제 : 1439 뒤집기
# 난이도  : 실버 4

S = input()

def logic(string):
    state = -1  # 이전 상태 저장
    zero = 0   # zero 뭉터기 개수
    one = 0   # one 뭉터기 개수

    for val in string:
        if state != val:
            state = val
            if val == '0': zero += 1
            elif val == '1': one += 1 
            
    return min(zero, one)

print(logic(S))