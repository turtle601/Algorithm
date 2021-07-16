import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = []

tree = [0] * (n*4)

for _ in range(n):
    lst.append(int(input()))

#최소 최대 구간 트리 생성
def min_max_tree(start, end, node):
    if start == end:
        tree[node] = [lst[start],lst[start]]
        return tree[node]

    mid = (start + end) // 2

    l = min_max_tree(start, mid, node*2)
    r = min_max_tree(mid+1, end, node*2+1)

    tree[node] = [min(l[0],r[0]), max(l[1],r[1])]

    return tree[node]

#구간 별 최대 최소 구하는 함수
def interval(start, end, node, left, right):
 
    if left > end or right < start:
        return [1000000001,0]

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    
    l = interval(start, mid, node*2, left, right)
    r = interval(mid + 1, end, node*2+1, left, right)         
    
    return [min(l[0],r[0]), max(l[1],r[1])]

min_max_tree(0,n-1,1)

for _ in range(m):
    a,b = map(int, input().split())
    result = interval(0,n-1,1,a-1,b-1)
    print(result[0],result[1])



           
