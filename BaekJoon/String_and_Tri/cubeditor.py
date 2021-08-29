# Cubeditor

import sys
input = sys.stdin.readline

word = input().strip()

#최대한 일치하는 접두사와 접미사의 길이를 구하는 함수
def find_pattern_length(p):
    j = 0

    table = [0] * len(p)

    for i in range(1,len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

    return max(table)

result = 0

# 접두사를 달리하여 두번 이상 중복되는 모든 단어를 구할 수 있다. 
for i in range(len(word)):
    pattern = word[i:]

    ans = find_pattern_length(pattern)

    result = max(result, ans)

print(result)    