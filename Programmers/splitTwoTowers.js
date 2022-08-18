// 프로그래머스 - 전력망 둘로 나누기

function solution(n, wires) {
  let result = Infinity;
  // 모든 연결 하나씩 끊어보기
  for (let i = 0; i < wires.length; i++) {
    const [v1, v2] = wires[i];
    // 2차원 배열 복사할 때는 이렇게 하자 -> splice 사용 X
    const removeOneWires = [...wires.slice(0, i), ...wires.slice(i + 1)];

    const graph = makeGraph(n, removeOneWires);
    const visitied = makeVisitied(n);

    const v1Count = bfs(v1, graph, visitied);
    const v2Count = bfs(v2, graph, visitied);

    result = Math.min(result, Math.abs(v1Count - v2Count));
  }

  return result;
}

function makeVisitied(n) {
  const visited = Array.from({ length: n + 1 }, () => false);
  visited[0] = null;

  return visited;
}

function makeGraph(n, wires) {
  const graph = Array.from({ length: n + 1 }, () => []);

  for (const [start, end] of wires) {
    graph[start].push(end);
    graph[end].push(start);
  }

  graph[0] = null;

  return graph;
}

// 트리 탐색하기
function bfs(v, graph, visited) {
  const queue = [v];
  visited[v] = true;

  let count = 1;

  while (queue.length > 0) {
    const now = queue.shift();

    for (const next of graph[now]) {
      if (!visited[next]) {
        count += 1;
        visited[next] = true;
        queue.push(next);
      }
    }
  }

  return count;
}

console.log(
  solution(9, [
    [1, 3],
    [2, 3],
    [3, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [7, 8],
    [7, 9],
  ])
);
console.log(
  solution(4, [
    [1, 2],
    [2, 3],
    [3, 4],
  ])
);
console.log(
  solution(7, [
    [1, 2],
    [2, 7],
    [3, 7],
    [3, 4],
    [4, 5],
    [6, 7],
  ])
);
