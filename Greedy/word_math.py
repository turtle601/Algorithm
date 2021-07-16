n = int(input())

dic = {}

for _  in range(n):
    word = str(input())
    n = len(word)
    # 해당 알파벳 자릿수를 알아낸다.
    for i in range(n):
        # 해당 알파벳이 dic에 없다면
        if word[i] not in dic.keys():
            dic[word[i]] = pow(10,n-1-i)
        
        # 있다면 +
        else:
            dic[word[i]] += pow(10,n-1-i)
       

#coef는 계수를 나타낸다. 
coef = list(dic.values()) 

#구간들을 내림차순으로 저장
coef.sort(reverse=True)

cnt = 9
sum = 0

for c in coef:
    sum += cnt * c
    cnt -= 1

print(sum) 




