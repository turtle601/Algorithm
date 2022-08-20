// 프로래머스 모음 사전
const alpha = ['A', 'E', 'I', 'O', 'U'];

function solution(word) {
  const wordList = word.split("");
  const n = wordList.length;

  let result = 0;

  for (let i = 0; i < n; i++) {
    const alphabet = wordList[i];
    result += countAlpha(alphabet, i);
  }

  return result;
}

// 해당 알파의 자릿수 구하기
function countAlpha(alphabet, startIdx) {
  if (alphabet === "A") {
    return 1;
  } else {
    let count = 0;
    
    for (let i = 0; i <= 4 - startIdx; i++) {
      count += Math.pow(5, i);
    }
    
    count = alpha.indexOf(alphabet) * count + 1;
    
    return count;
  }
}

function solution2(word) {
    const alphas = ['A', 'E', 'I', 'O', 'U'];
    let isFind = false;
    let ans = -1;

    // 어차피 경우의 수는 6^6 = 46,656 밖에 없으니까 완탐 돌려버림
    const dfs = (depth, make) => {
        isFind = make == word;
        ans++;

        if (depth == 5 || isFind) return;

        for (let i = 0; i < 5; i++) {
            if (isFind) break;

            dfs(depth + 1, make + alphas[i]);
        }
    }

    dfs(0, "");

    return ans;
}


console.log(solution("AAAAE")) // 6
console.log(solution("AAAE")) // 10
console.log(solution("I")) // 1563
console.log(solution("EIO")) // 1189