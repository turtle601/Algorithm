// 프로그래머스 보석 쇼핑
const hasAllGerms = (gemsSlice, gems) => {
  const gemsSet = new Set([...gems]);
  const gemsSliceSet = new Set([...gemsSlice]);

  return [...gemsSet].length === [...gemsSliceSet].length;
};

function solution(gems) {
  let left = 0;
  let right = 0;

  const n = gems.length;

  let result = [];

  while (left <= right && right <= n - 1) {
    if (!hasAllGerms(gems.slice(left, right + 1), gems)) {
      right += 1;
    } else {
      result.push([left, right]);
      left += 1;
    }
  }

  result.sort((x, y) => x[1] - x[0] - (y[1] - y[0]));

  return result[0].map((v) => v + 1);
}

console.log(
  solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
);

console.log(solution(["AA", "AB", "AC", "AA", "AC"]));
console.log(solution(["XYZ", "XYZ", "XYZ"]));
console.log(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]));
