n,row,col=map(int, input().split())

cnt = 0

while n > 1:
    size = 2 ** (n-1)

    #1사분면에 있다면
    if row < size and col >= size:
        cnt += pow(size,2)
        col -= size
    #2사분면에 있다면
    elif row >= size and col < size:
        cnt += pow(size,2) * 2
        row -= size
    #3사분면에 있다면    
    elif row >= size and col >= size:
        cnt += pow(size,2) * 3
        row -= size
        col -= size
    
    n -= 1                
# n == 1일때

#1사분면에 있다면
if row == 0 and col == 1:
    cnt += 1
#2사분면에 있다면
elif row == 1 and col == 0:
    cnt += 2
#3사분면에 있다면    
elif row == 1 and col == 1:
    cnt += 3 

print(cnt)      

