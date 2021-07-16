str1 = str(input())
str2 = str(input())

# dp를 2차원 배열로 만든다. 
dp = [[""] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(str1) + 1):
    for j in range(1,len(str2) + 1):
        # 만약 같은 문자가 나온다면 
        if str1[i-1] == str2[j-1]:
            
            # dp[i-1][j-1]에다가 (같다고 나온)문자 추가한다.
            dp[i][j] = dp[i-1][j-1] + str1[i-1]

        #같은 문자가 나오지 않는다면
        else:    

            #길이가 더 큰 문자를 채운다. 
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

ans = dp[-1][-1]

if ans == "":
    print(0)
else:
    print(len(ans))
    print(ans)    


