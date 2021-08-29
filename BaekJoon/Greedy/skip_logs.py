# 통나무 건너 뛰기

# 통나무 높이 리스트를 내림차순으로 정렬한다.
# 제일 높은 리스트 값 A은 양옆에 그 다음으로 큰 두개의 노드(B,C)가 차지 하게 되고
# 그 다음 두 노드는 D,E는 B - D, C - E로 연결되게 된다. 

# 따라서 D-B-A-C-E 로 연결되게 된다. 이렇게 연결할 시 통나무의 난이도를 가장 많이 줄일 수 있다.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())

    lst = list(map(int, input().strip().split()))
    
    # 통나무 높이 리스트를 내림차순으로 정렬한다.
    lst.sort(reverse=True)

    result = []

    for i in range(n-2):
        # 제일 높은 리스트 값 A은 양옆에 그 다음으로 큰 두개의 노드(B,C)가 차지 하게 되고
        if i == 0:
            result.append(lst[i] - lst[i+1])
            result.append(lst[i] - lst[i+2])

        else:
            # 그 다음 두 노드는 D,E는 B - D, C - E로 연결되게 된다. 
            result.append(lst[i] - lst[i+2]) 

    print(max(result))


