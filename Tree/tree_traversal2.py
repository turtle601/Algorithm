import sys
sys.setrecursionlimit(10**6)

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0]*(n+1)

for i in range(n):
    idx[in_order[i]] = i

#전위 순회
def div(in_start, in_end, p_start, p_end):
    if(in_start > in_end) or (p_start > p_end):
        return    
    
    root = post_order[p_end]
    print(root,end=" ")
    left = idx[root] - in_start #왼쪽 인자 개수
    right = in_end - idx[root]  #오른쪽 인자 개수

    div(in_start, in_start+left-1,p_start, p_start+left-1) #왼쪽
    div(in_end-right+1, in_end, p_end-right, p_end-1)      #오른쪽

div(0,n-1,0,n-1)    
