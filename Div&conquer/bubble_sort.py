n = int(input())

lst = list(map(int, input().split()))

result = 0

def srt(lst):
    global result
    #lst의 길이가 1이 될 때까지 분할
    if len(lst) <= 1:
        return lst

    #분할
    a = srt(lst[:len(lst) // 2])
    b = srt(lst[len(lst) // 2:])
    
    #병합
    i = 0
    j = 0
    cnt = 0

    #매 순간마다 정렬하기 위해 리셋
    merg = []

    while i < len(a) and j < len(b):
        #왼쪽 리스트의 값이 들어올 때
        if a[i] <= b[j]:
            merg.append(a[i])
            i += 1
            
            result += cnt
        #오른쪽 리스트의 값이 들어올 때    
        else:
            merg.append(b[j])
            j += 1
            cnt += 1
    
    #두 리스트 중 한 리스트의 값이 모두 소진 되었을 때
    while i < len(a):
        merg.append(a[i])
        result += cnt
        i += 1

    while j < len(b):
        merg.append(b[j])
        j += 1
        
    return merg  

srt(lst)
    
print(result)
        
