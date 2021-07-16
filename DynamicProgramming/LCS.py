### 백준
## LCS 9251번
# DynamicProgramming

word1 = list(input())
word2 = list(input())

dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]

for i in range(1,len(word2)+1):
    for j in range(1,len(word1)+1):
        if word2[i-1] == word1[j-1]:
            # dp 대각선 위의 값 + 1
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            # dp 왼쪽 값과 윗 값을 비교, 큰 값을 채워 넣는다.
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 

# answer
print(dp[-1][-1])               



