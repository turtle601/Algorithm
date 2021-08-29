import sys
input = sys.stdin.readline

word = input().strip()
pattern = input().strip()

#패턴이 같은 문자가 있을 때 그 문자열의 길이를 저장
table = [0] * len(pattern)

def KMP(word,pattern):
    
    j = 0

    for i in range(len(word)):
        
        while j > 0 and word[i] != pattern[j]:
            # table이 접두사와 접미사가 어느 정도의 길이까지 일치하는지를 나타내준다. 
            # 따라서 일치하지 않을 경우 그 전에는 얼마나 일치했는지 알아야한다. 
            # 따라서 table[j-1]의 값을 j로 설정하여 다시 한번 pattern이 일치하는지 확인
            j = table[j-1]

        if word[i] == pattern[j]:
            # 같은 패턴을 찾았을 때 그 패턴의 시작점(word에서) 츌력
            if j == len(pattern) - 1:
                #인덱스 값 출력
                print("find", end = " ")
                print(i - len(pattern) + 2)
                # 일치한 부분 다음 부분으로 j를 보내 효율적으로 또 똑같은 패턴을 찾을 수 있게 한다.    
                j = table[j]

            else:
                j += 1        


#최대로 일치하는 접두사와 접미사를 구하는 함수
def find_pattern_length(pattern):

    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        # 문자열이 같을 경우 
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

find_pattern_length(pattern)
KMP(word,pattern)

#https://bowbowbow.tistory.com/6