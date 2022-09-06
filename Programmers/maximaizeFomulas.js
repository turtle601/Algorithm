// 수식 최대화
function solution(expression) {
  const operand = expression.split(/[\+\-\*]/g);
  const operator = expression.split(/[0-9]/g).filter((v) => v !== "");

  const operatorSet = [...new Set([...operator])];

  const perms = permutations(operatorSet, operatorSet.length);

  let i = 0;
  let formulation = [];

  while (i < operand.length + operator.length) {
    if (i % 2 === 0) {
      formulation.push(operand[parseInt(i / 2)]);
    } else {
      formulation.push(operator[parseInt(i / 2)]);
    }

    i++;
  }

  return getResult(perms, formulation);
}

function permutations(arr, n) {
  if (n === 1) return arr.map((v) => [v]);
  const result = [];

  arr.forEach((fixed, idx, arr) => {
    const rest = arr.filter((_, index) => index !== idx);
    const perms = permutations(rest, n - 1);
    const combine = perms.map((v) => [fixed, ...v]);
    result.push(...combine);
  });

  return result;
}

function getResult(perms, formulation) {
  let max = 0;

  for (const perm of perms) {
    let copy = [...formulation];

    for (const op of perm) {
      copy = getStackCal(op, copy);
    }

    max = Math.max(max, Math.abs(+copy.join("")));
  }

  return max;
}

function getStackCal(perm, formulation) {
  let stack = [];

  for (const op of formulation) {
    if (stack.length > 1 && stack[stack.length - 1] === perm) {
      stack.pop();
      stack[stack.length - 1] = calculation(stack[stack.length - 1], op, perm);
    } else {
      stack.push(op);
    }
  }

  return stack;
}

function calculation(x, y, op) {
  if (op === "+") {
    return +x + +y;
  } else if (op === "-") {
    return +x - +y;
  } else {
    return +x * +y;
  }
}

console.log(solution("100-200*300-500+20")); // 60420
console.log(solution("50*6-3*2")); // 300
