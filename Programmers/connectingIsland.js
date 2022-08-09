// 프로그래머스 섬 연결하기

function find(parent, x) {
  if (parent[x] === x) {
    return x;
  }

  return (parent[x] = find(parent, parent[x]));
}

function union(parent, x, y) {
  const parentX = find(parent, x);
  const parentY = find(parent, y);

  if (parentX < parentY) {
    parent[parentY] = parentX;
  } else {
    parent[parentX] = parentY;
  }
}

function compare(parent, x, y) {
  return find(parent, x) === find(parent, y);
}

// kruskal 알고리즘
function solution(n, costs) {
  const sortedCosts = costs.sort((x, y) => x[2] - y[2]);
  const disjoint = Array.from({ length: n }, (_, id) => id);

  let result = 0;

  for (const [start, end, cost] of sortedCosts) {
    if (!compare(disjoint, start, end)) {
      result += cost;
      union(disjoint, start, end);
    }
  }

  return result;
}

console.log(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ])
);
