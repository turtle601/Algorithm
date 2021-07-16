n = int(input())

lst = list(input())

# 접두사 접미사가 얼마나 같은지 확인하는 table을 만드는 함수
def make_prefix_suffix_table(pattern):
    j = 0

    for i in range(1,len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

table = [0] * n
make_prefix_suffix_table(lst)

# 전체길이 - (접두사와 접미사가 어느 정도 같은지 나타내는 값) 
print(n - table[-1])