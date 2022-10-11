const DIVIDE_NUMBER = 1000000007;

function solution(n, money) {
  money = money.sort((x, y) => x - y);

  const dp = Array.from({ length: n + 1 }, () => 0);

  dp[0] = 1;

  for (const mon of money) {
    for (let i = mon; i <= n; i++) {
      dp[i] += dp[i - mon];
    }
  }

  return dp[dp.length - 1] % DIVIDE_NUMBER;
}

console.log(solution(5, [1, 2, 5])); // 4
console.log(solution(5, [2, 3, 5])); // 4
