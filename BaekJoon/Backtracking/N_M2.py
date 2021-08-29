# 백준 N과 M(2)
# 15650번
# 백트래킹

# 원래 나의 풀이
# from itertools import combinations

# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())

# lst = [i for i in range(1,n+1)]

# result = []
# # 조합들의 경우의 수를 result리스트에 담는다. 
# result.extend(combinations(lst,m))

# # 튜플의 값들 출력
# for i in result:
#     print(*i)

# 다른 풀이
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

visited = [False] * (n + 1)
def dfs(depth):
    
    #리스트의 개수가 m이면 역추적을 중단하고 다른 길을 찾아본다. 
    if depth == m:
        print(*lst)
        return 
    
    for i in range(1,n+1):
        
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            dfs(depth+1)
            lst.pop()
            # 혹시라도 방문한 자국이 있을 경우 리셋 한다. 
            # dfs함수를 리턴하고 난 다음이므로 앞서 확인한 노드 이후에 노드만 리셋해야 한다. 
            visited[i+1:] = [False] * (n - i) 
 
lst = []
dfs(0)