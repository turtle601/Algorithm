n = int(input())

# 주소값 리스트로 된 원본 W의 항목들을 다시 알파벳 리스트로 반환하는 함수 
def find_alpha(lst,lenA):
    ans = []

    for i in lst:
        #알파벳으로 돌려줄 때 해당 주소값 +=1 , %= len(A) 를 하여 계산
        i += 1
        i %= lenA
        ans.append(dic1[i])

    return ans

# 알파벳 리스트로 된 원본 W의 항목들을 주소값 리스트로 반환하는 함수
def find_address(lst):
    ans = []

    for i in lst:
        ans.append(dic2[i])

    return ans

# 접두사와 접미사가 얼만큼 일치하는지 나타내는 table을 구하는 함수
def make_prefix_suffix(pattern):
    j = 0

    for i in range(1,len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

# KMP 알고리즘
def KMP(word,pattern):
    global count
    j = 0

    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:
            j = table[j-1] 

        if word[i] == pattern[j]:
            if j == len(pattern) - 1:
                count += 1
                j = table[j]
            else:
                j += 1


for _ in range(n):
    A = list(input())     # 알파벳 순서
    W = list(input())     # 원문
    S = list(input())     # 암호화된 문자열

    dic1 = {} # 주소: 값
    dic2 = {} # 값  : 주소

    result = []

    for i,val in enumerate(A):
        dic1[i] = val
        dic2[val] = i

    for i in range(0,len(A)):
        
        count = 0
        #i가 0일 때는 바뀌지 않으므로
        if i != 0:
            # 주소값을 변경하여 W계산
            lst = find_address(W)
            W = find_alpha(lst,len(A))
    
        table = [0] * len(W)
        make_prefix_suffix(W)
        KMP(S,W)

        if count == 1:
            result.append(i)

    if len(result) == 0:
        print("no solution")

    elif len(result) == 1:
        print("unique:", result[0])
    
    else:
        result.sort()
        print("ambiguous:", end = " ")
        print(*result)

