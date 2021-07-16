# 백준 N과 M(5)
# 15654번
# 백트래킹

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

ans = []

visited = [False] * len(lst) 

def dfs(depth):
    if depth == m:
        print(*ans)
        return

    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            ans.append(lst[i])
            dfs(depth + 1)
            # 해당 노드에 대해서만 False 해주어서 모든 순열을 다 따질 수 있게 해준다. 
            visited[i] = False
            ans.pop()

dfs(0)


# import sys
# from itertools import permutations

# input = sys.stdin.readline

# n,m = map(int, input().split())

# lst = list(map(int, input().split()))
# lst.sort()

# answer = []

# answer.extend(permutations(lst,m))

# for ans in answer:
#     print(*ans)