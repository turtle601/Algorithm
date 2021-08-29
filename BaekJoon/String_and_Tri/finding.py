#찾기

#문제 예제에 공백도 있다면 sys사용 금지
word = input()
pattern = input()

table = [0] * len(pattern)

#최대한 일치하는 접두사와 접미사의 길이를 구하는 함수
def find_pattern_length(pattern):
    j = 0

    for i in range(1,len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j    

def KMP(word,pattern):
    global cnt
    global result
    j = 0

    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:

            j = table[j-1]

        if word[i] == pattern[j]:
            if j == len(pattern) - 1:
                # 같은 패턴을 찾았을 때 그 패턴의 시작점(word에서)
                result.append(i-len(pattern)+2)
                cnt += 1
                # 일치한 부분 다음 부분으로 j를 보내 효율적으로 또 똑같은 패턴을 찾을 수 있게 한다.       
                j = table[j]

            else :
                j += 1

cnt = 0
result = []

find_pattern_length(pattern)
KMP(word,pattern)

print(cnt)
print(*result)