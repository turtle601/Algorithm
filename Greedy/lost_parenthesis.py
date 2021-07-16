k = str(input())

plus = []
minus = []

flag = True

for i in range(len(k)):
    if k[i] == '-':
        flag = False
        
    if flag == True:
        plus.append(k[i])
    elif flag == False:
        minus.append(k[i])    

c = 0

sum1 = 0
sum2 = 0

for i in range(len(plus)-1,-1,-1):
    if plus[i] == '+' or plus[i] == '-':
        c = 0
    else:
        sum1 += int(plus[i]) * pow(10,c)
        c += 1    

c = 0

for i in range(len(minus)-1,-1,-1):
    if minus[i] == '+' or minus[i] == '-':
        c = 0
    else:
        sum2 += int(minus[i]) * pow(10,c)
        c += 1    

print(sum1 - sum2)
