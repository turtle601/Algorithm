class MooGame {
  constructor() {
    this.n = 0;
  }

  getInput(line) {
    this.n = line;
  }

  S() {
    let n = 0;
    let str = [];

    while (str.length < this.n) {
      if (n === 0) {
        str = ["m", "o", "o"];
      } else {
        str = [...str, "m", ...new Array(n + 2).fill("o"), ...str];
      }

      n += 1;
    }

    return str[this.n - 1];
  }
}

(function solution() {
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const moo = new MooGame();

  rl.on("line", function (line) {
    moo.getInput(line);
  }).on("close", function () {
    console.log(moo.S());
  });
})();
