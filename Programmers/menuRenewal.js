// 프로그래머스 메뉴 리뉴얼

function combinations(arr, n) {
  if (n === 1) return arr.map((v) => [v]);

  const result = [];

  arr.forEach((fixed, index, arr) => {
    const rest = arr.slice(index + 1);
    const combi = combinations(rest, n - 1);
    const combine = combi.map((v) => [fixed, ...v]);
    result.push(...combine);
  });

  return result;
}

function solution(orders, course) {
  const result = [];

  orders = orders.map((order) => order.split("").sort());

  for (const count of course) {
    const map = new Map();

    for (const order of orders) {
      makeCombiMap(count, order, map);
    }

    result.push(...getMaxItem(map));
  }

  return result.sort();
}

function makeCombiMap(count, order, map) {
  const list = combinations(order, count);

  for (const item of list) {
    const itmeString = item.join("");
    const defaultItem = map.get(itmeString) || 0;
    map.set(itmeString, defaultItem + 1);
  }
}

function getMaxItem(map) {
  const result = [];

  const max = Math.max(...map.values());

  if (max < 2) return [];

  for (const [key, value] of map) {
    if (value === max) {
      result.push(key);
    }
  }

  return result;
}

console.log(
  solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
); // ["AC", "ACDE", "BCFG", "CDE"]

console.log(
  solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
); // ["ACD", "AD", "ADE", "CD", "XYZ"]

console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4])); //["WX", "XY"]
