// 프로그래머스 비밀지도
function solution(n, arr1, arr2) {
  return new Array(n)
    .fill(0)
    .map((_, id) => arr1[id] | arr2[id])
    .map((v) =>
      [...v.toString(2).padStart(n, "0")]
        .map((v) => (v == 1 ? "#" : " "))
        .join("")
    );
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]));
