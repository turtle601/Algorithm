// 프로그래머스 단어 퍼즐
function solution(strs, t) {
  const dp = new Array(t.length + 1).fill(0);
  const strsSet = new Set(strs);

  for (let i = 1; i < t.length + 1; i++) {
    dp[i] = Infinity;

    for (let j = 1; j < Math.min(i + 1, 6); j++) {
      const value = t.slice(i - j, i);

      if (strsSet.has(value)) {
        dp[i] = Math.min(dp[i], dp[i - j] + 1);
      }
    }
  }

  return dp[dp.length - 1] === Infinity ? -1 : dp[dp.length - 1];
}

console.log(solution(["ba", "na", "n", "a"], "banana"));
console.log(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"));
console.log(solution(["ba", "an", "nan", "ban", "n"], "banana"));
