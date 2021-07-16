# leetcode 125
# Valid_Palindrome

import re
# 정규 표현식을 활용한 효율적인 풀이
def isPalindrome(s):
    s = s.lower()
    
    # a-z, 0-9까지 단어를 제외한 단어들을 모두 ''로 대체하겠다.
    s = re.sub('[^a-z0-9]','',s)
    
    return s == s[::-1] 


