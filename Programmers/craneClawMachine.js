// 프로그래머스 Level 1 - 크레인 인형뽑기
function solution(board, moves) {
  const n = board.length;
  const map = new Map();

  for (let i = 0; i < n; i++) {
    map.set(i, []);
    for (let j = 0; j < n; j++) {
      if (board[j][i] !== 0) {
        map.set(i, [...map.get(i), board[j][i]]);
      }
    }
  }

  const stack = [];

  let count = 0;

  for (const move of moves) {
    if (map.get(move - 1).length > 0) {
      const value = map.get(move - 1).shift();
      console.log(value, stack[stack.length - 1]);
      if (stack.length > 0 && stack[stack.length - 1] === value) {
        count += 1;
        stack.pop();
      } else {
        stack.push(value);
      }
    }
  }

  return count * 2;
}

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
); // 4
