// 프로그래머스 단어 퍼즐
function solution(strs, t) {
  const n = t.length;
  const dp = new Array(n).fill(Infinity);
  const strsSet = new Set(strs);

  for (let i = 0; i < t.length; i++) {
    for (let j = i; j > -1; j--) {
      const value = t.slice(j, i + 1);

      if (strsSet.has(value)) {
        if (j === 0) {
          dp[i] = 1;
        } else {
          dp[i] = Math.min(dp[i], dp[j - 1] + 1);
        }
      }
    }
  }

  return dp[dp.length - 1] === Infinity ? -1 : dp[dp.length - 1];
}

console.log(solution(["ba", "na", "n", "a"], "banana"));
console.log(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"));
console.log(solution(["ba", "an", "nan", "ban", "n"], "banana"));
