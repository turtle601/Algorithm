# 프로그래머스
# 카카오 2019 블라인드 채용 출제 문제 
# 후보키

# 입력값
relation = [["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]]

from itertools import combinations

# relation의 주소값 combination 조합들을 
# 원래의 값들의 조합으로 바꾸는 함수
def make_table(lst,row,col,relation):
    
    ans = []

    for i in range(row):
        option = []

        for j in lst:
            option.append(relation[i][j])

        ans.append(option)

    return ans    

def solution(relation):
        
    row = len(relation)     #세로 축
    col = len(relation[0])  #가로 축

    address = [i for i in range(0,col)]

    comb = []
    
    #후보키의 모든 조합을 comb리스트에 저장
    for i in range(1,col+1):
        comb.extend(map(tuple,combinations(address,i)))

    unique = []

    ## 유일성 만족
    for com in comb:    
        flag = False
        lst = make_table(com,row,col,relation)

        # 각 항목에 똑같은 값들이 있는지 확인한다. 
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i == j:
                    continue

                else:
                    if lst[i] == lst[j]:
                        flag = True
                        break
        
            if flag == True:
                break        
        
        # 없다면 유일성의 속성을 가지고 있기 때문에 unique리스트에 넣어준다. 
        if flag == False:
            unique.append(com)

    # set으로 자료형을 묶기 위해서는 각 리스트의 원소들이 해쉬가 있는 값(set, 숫자)이어야 한다.
    answer = set(unique)

    ### 최소성 만족
    for i in range(len(unique)):
        for j in range(len(unique)):
            if i == j:
                continue

            else:
                #만약 unique에 있는 임의의 두 원소를 비교하여 부분집합일 경우 그 원소를 제거한다. 
                if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                    # set 자료형에서만 쓸 수 있는 discard함수를 통해 해당값이 있으면 지울 수 있고 없어도 오류가 발생하지 않을 수 있다.
                    answer.discard(unique[j])

    return len(answer)

# 답 출력
print(solution(relation))    