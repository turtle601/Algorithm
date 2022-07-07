let result = "";

const divideMoo = (wholeLen, depth, N) => {
  if (depth === 0) {
    return N === 0 ? "m" : "o";
  }

  const div1 = Math.floor((wholeLen - (depth + 3)) / 2);
  const div2 = div1 + depth + 3;

  if (N < div1) {
    return divideMoo(div1, depth - 1, N);
  } else if (N < div2) {
    return div1 === N ? "m" : "o";
  } else {
    return divideMoo(div1, depth - 1, N - div2);
  }
};

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

    result = divideMoo(mooLen, i, N);
  }).on("close", function () {
    console.log(result);
  });
})();
