// class MooGame {
//   constructor() {
//     this.n = 0;
//   }

//   getInput(line) {
//     this.n = line;
//   }

//   S() {
//     let n = 0;
//     let str = [];

//     while (str.length < this.n) {
//       if (n === 0) {
//         str = ["m", "o", "o"];
//       } else {
//         str = [...str, "m", ...new Array(n + 2).fill("o"), ...str];
//       }

//       n += 1;
//     }

//     return str[this.n - 1];
//   }
// }

let result = "";

(function solution() {
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.on("line", function (line) {
    const N = line - 1;

    let mooLen = 0;
    let i = -1;

    while (mooLen < N + 1) {
      i += 1;

      if (i === 0) {
        mooLen += 3;
      } else {
        mooLen = 2 * mooLen + i + 3;
      }
    }

    const moo = (wholeLen, depth, N) => {
      if (depth === 0) {
        return N === 0 ? "m" : "o";
      }

      const div1 = Math.floor((wholeLen - (depth + 3)) / 2);
      const div2 = div1 + depth + 3;

      if (N < div1) {
        return moo(div1, depth - 1, N);
      } else if (N < div2) {
        return div1 === N ? "m" : "o";
      } else {
        return moo(div1, depth - 1, N - div2);
      }
    };

    result = moo(mooLen, i, N);
  }).on("close", function () {
    console.log(result);
  });
})();
