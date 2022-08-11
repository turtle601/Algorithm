function solution(n) {
  const queen = new Array(n).fill(0);

  return dfs(queen, n, 0);
}

function dfs(queen, n, row) {
  let count = 0;

  if (row === n) {
    return 1;
  }

  for (let i = 0; i < n; i++) {
    queen[row] = i;
    if (check(queen, row)) {
      count += dfs(queen, n, row + 1);
    }
  }

  return count;
}

function check(queen, row) {
  for (let i = 0; i < row; i++) {
    if (
      queen[i] === queen[row] ||
      Math.abs(queen[i] - queen[row]) === row - i
    ) {
      return false;
    }
  }

  return true;
}

console.log(solution(4));
