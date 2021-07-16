### leetcode 49 
## Group Anagrams
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

import collections

# 입력값
strs = ["eat","tea","tan","ate","nat","bat"]

# key값이 없을 때 dic에 입력시 KeyError가 나타난다. 그래서 KeyError방지를 위해 다음과 같이 dic 설정
anagrams = collections.defaultdict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)


print(anagrams.values())    