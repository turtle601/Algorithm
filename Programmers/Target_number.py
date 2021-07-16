### 프로그래머스 Level2
## 타겟 넘버


def solution(numbers, target):

    graph = [[num, -num] for num in numbers]

    cnt = [0]

    def dfs(n, sum):

        if n == len(numbers):
            if sum == target:
                cnt[0] += 1
            return True

        for i in range(2):
            dfs(n + 1, sum + graph[n][i])

        return False

    dfs(0, 0)

    return
