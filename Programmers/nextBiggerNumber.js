const get2Bit = (num) => {
  return num.toString(2).split("").filter(v => v === "1").length;
}

function solution(n) {
  let result = n + 1;
  const nOneCount = get2Bit(n)

  while(nOneCount !== get2Bit(result)){
      result += 1;
  }

  return result
}