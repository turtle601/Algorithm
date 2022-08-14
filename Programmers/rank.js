// 프로그래머스 순위
function solution(n, result) {
  const [winGraph, loseGraph] = makeGraph(result, n);

  let count = 0;

  for (let i = 1; i <= n; i++) {
    const visited = Array.from({ length: n + 1 }, () => false);
    dfs(i, n, winGraph, visited, 1);
    dfs(i, n, loseGraph, visited, 1);

    count += visited.filter((v) => !!v).length === n;
  }

  return count;
}

function dfs(v, n, graph, visited, depth) {
  visited[v] = true;

  if (depth === n || graph[v].length === 0) {
    return depth;
  }

  for (const val of graph[v]) {
    if (!visited[val]) {
      dfs(val, n, graph, visited, depth + 1);
    }
  }
}

function makeGraph(result, n) {
  const winGraph = Array.from({ length: n + 1 }, () => []);
  const loseGraph = Array.from({ length: n + 1 }, () => []);

  winGraph[0] = null;
  loseGraph[0] = null;

  for (const [w, l] of result) {
    winGraph[w].push(l);
    loseGraph[l].push(w);
  }

  return [winGraph, loseGraph];
}

console.log(
  solution(5, [
    [4, 3],
    [4, 2],
    [3, 2],
    [1, 2],
    [2, 5],
  ])
); // 2
