// 프로그래머스 피로도
function solution(k, dungeons) {
  const n = dungeons.length;

  return permutations(dungeons, n).reduce(
    (pre, cur) => Math.max(pre, countPiroad(cur, k)),
    0
  );
}

function permutations(arr, n) {
  if (n === 1) return arr.map((v) => [v]);

  const result = [];

  arr.forEach((fixed, idx, arr) => {
    const rest = arr.filter((_, id) => id !== idx);
    const perms = permutations(rest, n - 1);
    const combine = perms.map((v) => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
}

function countPiroad(arr, k) {
  let count = 0;

  for (const [rest, usage] of arr) {
    if (rest <= k) {
      k -= usage;
      count += 1;
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
