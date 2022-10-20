function solution(arr) {
  const stack = [];

  for (const item of arr) {
    if (stack.length > 0 && stack[stack.length - 1] === item) {
      stack.pop();
    }

    stack.push(item);
  }

  return stack;
}