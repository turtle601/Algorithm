// 프로그래머스 1차 뉴스 클러스터링

function solution(str1, str2) {
  const result1 = doSlice(str1);
  const result2 = doSlice(str2);

  const intersetion = getIntersection(result1, result2);
  const union = getUnion(result1, result2, intersetion);

  if (intersetion === 0 && union === 0) {
    return 65536;
  } else {
    return Math.floor((intersetion / union) * 65536);
  }
}

function doSlice(str) {
  let result = [];

  for (let i = 0; i < str.length; i++) {
    if (i < str.length - 1) {
      const two = str.slice(i, i + 2).toLowerCase();

      if (checkTwo(two)) result.push(two);
    }
  }

  return result;
}

function checkTwo(str) {
  const check = str.match(/[a-z]/g);

  if (check !== null && check.length === 2) {
    return true;
  }

  return false;
}

function getIntersection(arr1, arr2) {
  const flag = [...arr1];

  return arr2.filter((v) => {
    let check = false;

    if (flag.includes(v)) {
      check = true;
      flag.splice(flag.indexOf(v), 1);
    }

    return check;
  }).length;
}

function getUnion(str1, str2, intersetion) {
  return str1.length + str2.length - intersetion;
}

console.log(solution("FRANCE", "french"));
console.log(solution("handshake", "shake hands"));
console.log(solution("aa1+aa2", "AAAA12"));
console.log(solution("E=M*C^2", "e=m*c^2"));
