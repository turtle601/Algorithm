### 프로그래머스 키 패드 누르기(카카오 인턴십)
## Level 2
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/67256

## 입력값
# a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
# print(a)
# b = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
# print(b)
# c = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
# print(c)


def solution(numbers, hand):

    result = []

    memory = [[3, 0], [3, 2]]

    def find_index(n):
        y = (n - 1) // 3
        x = (n - 1) % 3

        return [y, x]

    for num in numbers:
        idx = find_index(num)
        if num in [1, 4, 7]:
            memory[0] = idx
            result.append("L")

        elif num in [3, 6, 9]:
            memory[1] = idx
            result.append("R")

        else:
            left = abs(idx[0] - memory[0][0]) + abs(idx[1] - memory[0][1])
            right = abs(idx[0] - memory[1][0]) + abs(idx[1] - memory[1][1])

            if left > right:
                memory[1] = idx
                result.append("R")
            elif left < right:
                memory[0] = idx
                result.append("L")
            else:
                if hand == "left":
                    memory[0] = idx
                    result.append("L")
                else:
                    memory[1] = idx
                    result.append("R")

    return "".join(result)
