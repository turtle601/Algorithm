// 프로그래머스 게임 맵 최단거리
const dx = [1, -1, 0, 0];
const dy = [0, 0, -1, 1];

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  const vistied = Array.from({ length: n }, () => Array(m).fill(false));

  return bfs(n, m, maps, vistied);
}

function bfs(n, m, maps, vistied) {
  const queue = [];
  queue.push([0, 0]);
  vistied[0][0] = true;

  while (queue.length > 0) {
    const [y, x] = queue.shift();

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;

      if (maps[ny][nx] === 1 && vistied[ny][nx] === false) {
        vistied[ny][nx] = true;
        maps[ny][nx] = maps[y][x] + 1;
        queue.push([ny, nx]);
      }
    }
  }

  return vistied[n - 1][m - 1] ? maps[n - 1][m - 1] : -1;
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
); // 11

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
  ])
); // - 1
