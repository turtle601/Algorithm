// 프로그래머스 이진 변환 반복하기
function solution(s) {
  s = s.split("");
  const result = [0, 0];

  while (s.length > 1) {
    s = removeZero(s, result);
    s = getDigitToBit(s.length);
    result[0] += 1;
  }

  return result;
}

function removeZero(s, result) {
  return s.filter((v) => {
    if (v === "0") {
      result[1] += 1;
      return false;
    } else {
      return true;
    }
  });
}

function getDigitToBit(num) {
  return num.toString(2).split("");
}

console.log(solution("110010101001")); // [3,8]
console.log(solution("01110")); // [3,3]
console.log(solution("1111111")); // [4,1]
