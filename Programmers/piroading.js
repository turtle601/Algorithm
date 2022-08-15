// 프로그래머스 피로도
function solution(k, dungeons) {
  const n = dungeons.length;
  const visited = Array.from({ length: n }, () => false);

  return dfs(k, 0, n, dungeons, visited);
}

function dfs(remain, depth, n, dungeons, visited) {
  if (depth === n) {
    return depth;
  }

  let count = depth;

  for (let i = 0; i < n; i++) {
    const [rest, usage] = dungeons[i];
    if (rest <= remain && !visited[i]) {
      visited[i] = true;
      count = Math.max(
        count,
        dfs(remain - usage, depth + 1, n, dungeons, visited)
      );
      visited[i] = false;
    }
  }

  return count;
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
); // 3
