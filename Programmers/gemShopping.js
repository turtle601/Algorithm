// 프로그래머스 보석 쇼핑

function solution(gems) {
  let left = 0;
  let right = 0;

  const gemsSize = [...new Set(gems)].length;
  const gemsMap = new Map();

  gemsMap.set(gems[0], 1);

  let answer = [0, gems.length - 1];

  while (left <= right && right < gems.length) {
    if (gemsMap.size === gemsSize) {
      if (right - left < answer[1] - answer[0]) {
        answer = [left, right];
      }

      gemsMap.set(gems[left], gemsMap.get(gems[left]) - 1);

      if (gemsMap.get(gems[left]) === 0) {
        gemsMap.delete(gems[left]);
      }

      left += 1;
    } else {
      right += 1;
      gemsMap.set(gems[right], (gemsMap.get(gems[right]) || 0) + 1);
    }
  }

  return answer.map((v) => v + 1);
}

console.log(
  solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
);

console.log(solution(["AA", "AB", "AC", "AA", "AC"]));
console.log(solution(["XYZ", "XYZ", "XYZ"]));
console.log(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]));
