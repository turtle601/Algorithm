const permutations = [];

const getPermutation = (arr, select, result = []) => {
  if (select === 1) {
    permutations.push(...arr.map((v) => [...result, v]));
    return;
  }

  for (let i = 0; i < arr.length; i++) {
    const rest = [...arr.slice(0, i), ...arr.slice(i + 1)];
    result.push(arr[i]);
    getPermutation(rest, select - 1, result);
    result.pop();
  }
};

getPermutation([1, 2, 3, 4], 3);

const combinations = [];

const getCombination = (arr, select, result = []) => {
  if (select === 1) {
    combinations.push(...arr.map((v) => [...result, v]));
    return;
  }

  for (let i = 0; i < arr.length; i++) {
    const rest = [...arr.slice(i + 1)];
    result.push(arr[i]);
    getCombination(rest, select - 1, result);
    result.pop();
  }
};

getCombination([1, 2, 3, 4], 3);

console.log(permutations);
console.log(combinations);
