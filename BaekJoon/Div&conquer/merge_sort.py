n = int(input())

lst = list(map(int, input().split()))

cnt = 0

def srt(lst):
    if len(lst) <= 1:
        return lst

    a = srt(lst[len(lst) // 2:])
    b = srt(lst[:len(lst) // 2])
    
    i = 0
    j = 0

    merg = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merg.append(a[i])
            i += 1
        else:
            merg.append(b[j])
            j += 1

    while i < len(a):
        merg.append(a[i])
        i += 1

    while j < len(b):
        merg.append(b[j])
        j += 1
        
    return merg  


print(srt(lst))
