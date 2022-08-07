// 프로그래머스 - 두 개 뽑아서 더하기

// 조합 구하기
function combinations(arr, n) {
  if (n === 1) return arr.map((v) => [v]);
  const result = [];

  arr.forEach((fixed, idx, arr) => {
    const rest = arr.slice(idx + 1);
    const combis = combinations(rest, n - 1);
    const combine = combis.map((v) => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
}

// 배열 총합 구하기
function sum(arr) {
  return arr.reduce((pre, cur) => pre + cur, 0);
}

// 풀이
function solution(numbers) {
  return [...new Set(combinations(numbers, 2).map((v) => sum(v)))].sort(
    (x, y) => x - y
  );
}
