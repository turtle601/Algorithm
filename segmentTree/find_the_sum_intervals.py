n,m,k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

# 구간 합 트리의 용량
tree = [0] * (n * 4)

# 구간 합 트리 생성
def make_tree(start, end, node):
    if start == end: 
        tree[node] = lst[start]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = make_tree(start, mid, node*2) + make_tree(mid+1,end,node*2+1)
    
    return tree[node]

#구간 합 더하기
def tree_sum(start, end, node, left, right):
    if (left > end) or (right < start):
        return 0

    if (left <= start) and (end <= right):
        return tree[node]

    mid = (start + end) // 2
    return tree_sum(start, mid, node*2,left,right) + tree_sum(mid+1,end, node*2+1,left, right)

#특정 원소 바꾸기
#fixed = 바꾸려는 값 - 원래 값
def change(start, end, node, idx, fixed):
    if idx < start or idx > end:
        return 
    
    tree[node] += fixed 
    if start == end:
        return

    mid = (start + end) // 2
    change(start, mid, node*2, idx, fixed)
    change(mid + 1, end, node*2+1 , idx, fixed)       

make_tree(0,n-1,1)


for _ in range(m+k):
    a,b,c = map(int, input().split())

    if a == 1:
        #fix = 값이 바뀔 때마다 추가로 더하거나 빼줘야 하는 값
        fix = c - lst[b-1]
        
        #lst의 값 c로 바꿔줘야함 
        lst[b-1] = c
        change(0,n-1,1,b-1,fix)
        
    elif a == 2:   

        result = tree_sum(0,n-1,1,b-1,c-1)
        print(result)
        
