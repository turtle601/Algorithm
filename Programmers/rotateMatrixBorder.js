const rotate = (query, graph) => {
  const [x1, y1, x2, y2] = query.map((v) => v - 1);

  let result = [];
  const idxList = [];

  // top
  for (let i = y1; i < y2; i++) {
    result.push(graph[x1][i]);
    idxList.push([x1, i]);
  }

  // right
  for (let i = x1; i < x2; i++) {
    result.push(graph[i][y2]);
    idxList.push([i, y2]);
  }

  // bottom
  for (let i = y2; i > y1; i--) {
    result.push(graph[x2][i]);
    idxList.push([x2, i]);
  }

  // left
  for (let i = x2; i > x1; i--) {
    result.push(graph[i][y1]);
    idxList.push([i, y1]);
  }

  result = [result.pop(), ...result];

  return [idxList, result];
};

function solution(rows, columns, queries) {
  const graph = new Array(rows)
    .fill(0)
    .map((_, idx) =>
      [...new Array(columns).keys()].map((v) => idx * columns + v + 1)
    );

  const result = [];

  for (const query of queries) {
    const [idxList, rotateList] = rotate(query, graph);
    result.push(Math.min(...rotateList));

    for (let i = 0; i < rotateList.length; i++) {
      const [x, y] = idxList[i];
      graph[x][y] = rotateList[i];
    }
  }

  return result;
}
