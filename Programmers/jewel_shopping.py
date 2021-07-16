### 프로그래머스
## 카카오 인턴쉽 Level - 3
## 보석 쇼핑

# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/67258

## 정확성은 모두 맞았지만 효율성 테스트 11~15를 통과하지 못한 문제....
# 입력 값:
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
# ["AA", "AB", "AC", "AA", "AC"]	[1, 3]
# ["XYZ", "XYZ", "XYZ"]	[1, 1]
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]


def solution(gems):

    n = len(set(gems))

    high = len(gems)

    dic = {}

    lst = []

    for idx, val in enumerate(gems):
        dic[val] = idx + 1

        if len(dic) == n:
            l = list(dic.values())
            a = min(l)
            b = max(l)

            if b - a < high:
                result = [a, b]
                high = b - a

    return result
