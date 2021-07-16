n = int(input())

#윗줄 
x = list(map(int, input().split())) 

#아랫줄
y = list(map(int, input().split())) 

x.append(0)
y.append(0)

#x항, y항 대소 비교 
def make_z(k):
    if y[k] > x[k]:
        return 1
    elif y[k] < x[k]:
        return -1

    else:
        return 0        

cnt = 0

while x !=y :
    for i in range(len(x)-1):
        if make_z(i) == 0:
                continue
        
        #연속인지 확인하기 위해서는 바로 옆의 항만 알면 해결할 수 있다. 
        if make_z(i) == make_z(i+1):
            
            #한 칸씩 점점 x = y 같아지게 해준다. 
            if make_z(i) == 1:
                x[i] += 1
            
            elif make_z(i) == -1:
                x[i] -= 1

        else:
            
            #연속이 아니면 cnt추가
            cnt += 1

            #한 칸씩 점점 x = y 같아지게 해준다. 
            if make_z(i) == 1:
                x[i] += 1

            elif make_z(i) == -1:
                x[i] -= 1
    print(x,cnt)

print(cnt)

