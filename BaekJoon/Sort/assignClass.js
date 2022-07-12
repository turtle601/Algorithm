let N = 0;
let input = [];
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
    } else if (lineNum <= N) {
      input.push(line.split(" ").map((v) => Number(v)));
    } else {
      throw new Error("input을 더 추가하시면 안됩니다!!");
    }
    lineNum++;
  }).on("close", function () {
    // sorting 하기 x축 sorting -> yc축 sorting
    // 2차원 배열 생성
    const n = input.length;

    input = input.sort((x, y) => x[0] - y[0] || x[1] - y[1]);
    const row = input[n - 1][1];

    let graph = new Array(n).fill(0).map(() => new Array(row + 1).fill(0));

    for (const [start, end] of input) {
      let flag = true;
      let i = 0;
      while (flag) {
        if (graph[i][start] === 0) {
          flag = false;
          for (let j = start; j < end; j++) {
            graph[i][j] = 1;
          }
        }

        i++;
      }
    }

    const result = graph.filter((v) => {
      return v.filter((val) => val === 0).length !== row + 1;
    }).length;

    console.log(result);

    // 배열 값 하나씩 2차원 배열에 삽입
    // 해당 구간은 1로 표시

    // 시작점 구간에 1로 표시 되어 있다면 밑에 부분에 표시 -> 재귀
  });
})();
