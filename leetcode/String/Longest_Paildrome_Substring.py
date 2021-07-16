### leetcode 5
## Longest_Paildrome_Substring
# 가장 긴 팰린드롬 부분 문자열을 출력하라. 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0  and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1

            return s[left + 1: right - 1]

        # 길이가 2보다 작을 경우 그 단어는 펠린드롬이다.
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)
        
        return result