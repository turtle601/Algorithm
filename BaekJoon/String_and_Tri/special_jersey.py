# 백준 - 스페셜 저지
A = input()     #첫째 줄
B = input()     #둘째 줄
ans = input()   #셋째 줄

table = [0] * len(ans)

#table 생성 - 접두사와 접미사의 일치 길이 여부 
def make_prefix_suffix(pattern):
    j = 0
    
    for i in range(1,len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

#KMP 알고리즘     
def KMP(word,pattern):
    global flag 
    
    j = 0

    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:
            j = table[j-1]

        if word[i] == pattern[j]:
            if j == len(pattern) - 1:
                flag = True
                return 
            
            else:
    
               j += 1         

#테이블 생성
make_prefix_suffix(ans)

#A와 ans를 비교해 일치하는 문자열이 있는지 확인 - flag 변수
flag = False
KMP(A,ans)

if flag == False:
    print("NO")
    exit()

#B와 ans를 비교해 일치하는 문자열이 있는지 확인 - flag 변수
flag = False
KMP(B,ans)

if flag == False:
    print("NO")

else:
    print("YES")        