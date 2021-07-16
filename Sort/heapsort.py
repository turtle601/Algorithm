# 힙 생성 알고리즘
def heapify(lst, idx, n):
    left = idx * 2
    right = idx * 2 + 1
    s_idx = idx
    if (left <= n and lst[s_idx] > lst[left]):
    	s_idx = left
	

    if (right <= n and lst[s_idx] > lst[right]):
        s_idx = right

    if s_idx != idx:
        lst[idx], lst[s_idx] = lst[s_idx], lst[idx]
        return heapify(lst, s_idx, n)

# 힙 소트
def heap_sort(lst):
    n = len(lst)
    lst = [0] + lst

    # 최소 힙 생성
    for i in range(n,0,-1):
        heapify(lst,i,n)

    # 제일 작은 값 추출
    for i in range(n,0,-1):
        print(lst[1], end = " ")
        lst[i],lst[1] = lst[1],lst[i]
        heapify(lst, 1, i-1)



heap_sort([5,3,4,2,1])