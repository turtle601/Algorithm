let N = 0;
let inputList = [];
let lineNum = 0;

(function solution() {
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.on("line", function (line) {
    if (lineNum === 0) {
      N = line;
    } else if (lineNum === 1) {
      inputList = line.split(" ").map((val) => Number(val));
    } else {
      throw new Error("input 허용횟수 넘김");
    }
    lineNum++;
  }).on("close", function () {
    let max = Number.MAX_SAFE_INTEGER;
    let result = [];
    let flag = false;

    inputList.sort((x, y) => x - y);

    for (let i = 0; i < N - 2; i++) {
      let left = i + 1;
      let right = N - 1;

      while (left < right) {
        const sum = inputList[i] + inputList[left] + inputList[right];

        if (Math.abs(sum) < max) {
          max = Math.abs(sum);
          result = [inputList[i], inputList[left], inputList[right]];
        }

        if (sum > 0) {
          right -= 1;
        } else if (sum < 0) {
          left += 1;
        } else {
          flag = true;
          break;
        }
      }

      if (flag) break;
    }

    console.log(result.join(" "));
  });
})();
