# 프로그래머스
# 카카오 2019 블라인드 채용 출제 문제 Level - 2
# 땅따먹기 

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

# def solution(land):

#     n = len(land)

#     for i in range(1,n):
#         land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])

#         land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])

#         land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])

#         land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])

#     answer = max(land[-1])
#     return answer



def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            print(land[i -1][: j],land[i - 1][j + 1:])
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
        
    return max(land[-1])

print(solution(land))    