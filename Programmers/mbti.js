// 프로그래머스 성격 검사 유형
const list = ["RT", "CF", "JM", "AN"];

function solution(survey, choices) {
  const charPoint = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  }

  const checkCount = (str, num) => {
    if (num < 4) {
      charPoint[str[0]] += 4 - num;
    } else if (num > 4) {
      charPoint[str[1]] += num - 4;
    } 
  }

  for (let i = 0; i < survey.length; i++) {
    checkCount(survey[i], choices[i]);
  }

  let result = "";

  for (const item of list) { 
    const [left, right] = item.split("");

    if (charPoint[left] >= charPoint[right]){
      result += left;
    } else {
      result += right;
    }
  }

  return result;
}

console.log(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]));
console.log(solution(["TR", "RT", "TR"],	[7, 1, 3]));