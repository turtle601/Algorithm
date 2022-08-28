// 거리두기 확인하기
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function solution(places) {
  const result = [];

  for (const place of places) {
    result.push(+waitingRoom(place));
  }

  return result;
}

const waitingRoom = (place) => {
  const n = place.length;
  const visited = Array.from({ length: n }, () => Array(n).fill(false));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (place[i][j] === "P") {
        const breakpoint = bfs(i, j, n, visited, place);
        if (!breakpoint) return false;
      }
    }
  }

  return true;
};

function countP(arr) {
  return arr.filter((v) => v === "P").length;
}

function bfs(i, j, n, visited, place) {
  const queue = [[i, j, 1]];
  const checked = ["P"];
  visited[i][j] = true;

  while (queue.length > 0) {
    const [y, x, depth] = queue.shift();

    if (countP(checked) > 1) {
      return false;
    }

    if (depth > 2) continue; // 최대 근접 경우의 수 : PP, POP

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (!visited[ny][nx] && place[ny][nx] !== "X") {
          visited[ny][nx] = true;
          queue.push([ny, nx, depth + 1]);
          checked.push(place[ny][nx]);
        }
      }
    }
  }

  return true;
}

console.log(
  solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
  ])
); // [1, 0, 1, 1, 1]
