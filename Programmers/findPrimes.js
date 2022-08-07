// 프로그래머스 소수 찾기

function solution(n) {
  const prime = [false, false, ...Array(n - 1).fill(true)];

  for (let i = 2; i * i <= n; i++) {
    if (prime[i]) {
      for (let j = i * 2; j <= n; j += i) {
        prime[j] = false;
      }
    }
  }

  return prime.filter((v) => !!v).length;
}
