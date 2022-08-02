// 프로그래머스 가장 먼 노드

function solution(n, edge) {
  const graph = Array.from(new Array(n + 1), () => []);
  const visited = new Array(n + 1).fill(0);

  for (const [now, next] of edge) {
    graph[now].push(next);
    graph[next].push(now);
  }

  const queue = [1];
  visited[1] = 1;

  while (queue.length > 0) {
    const x = queue.shift();

    for (const next of graph[x]) {
      if (visited[next] === 0) {
        visited[next] = visited[x] + 1;
        queue.push(next);
      }
    }
  }

  return visited.filter((v) => v === Math.max(...visited)).length;
}
