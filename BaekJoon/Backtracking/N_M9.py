# from itertools import permutations
# import sys
# input = sys.stdin.readline

# itertools를 사용하여 푼 풀이
# n,m = map(int, input().split())

# lst = list(map(int, input().split()))

# result = []

# result.extend(permutations(lst,m))

# result = list(set(result))

# result.sort()

# for ans in result:
#     print(*ans)

#백트래킹을 사용해서 푼 문제
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = list(map(int, input().split()))

visited = [False] * len(lst)

ans = []

result = []

def dfs(depth):
    
    if depth == m:
        result.append(tuple(ans))

        return

    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            ans.append(lst[i])
            dfs(depth+1)
            # 해당 노드에 대해서만 False 해주어서 모든 순열을 다 따질 수 있게 해준다. 
            visited[i] = False
            ans.pop()


dfs(0)

# 중복되는 값들이 있으면 set 자료구조를 통해 없애주고 다시 list로 감싼다. 
result = list(set(result))

# result안에 있는 값들을 sort()
result.sort()

for answer in result:
    print(*answer)