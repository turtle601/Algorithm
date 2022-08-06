// 프로그래머스 큰 수 만들기 - 그리디

function solution(number, k) {
  number = number.split("").map((v) => Number(v));

  const stack = [];
  let count = 0;

  for (const num of number) {
    while (count < k && stack[stack.length - 1] < num) {
      stack.pop();
      count++;
    }
    stack.push(num);
  }

  // 엣지 케이스 - 987654321, 4
  while (count < k) {
    stack.pop();
    count++;
  }

  return stack.join("");
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
