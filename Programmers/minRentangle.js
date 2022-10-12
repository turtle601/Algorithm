// 프로그래머스 최소직사각형
function solution(sizes) {
  const copySizes = [];

  for (const size of sizes){
    copySizes.push(size.sort((x,y) => x - y));
  }
  
  const col = copySizes.map(v => v[0]);
  const row = copySizes.map(v => v[1]);

  return Math.max(...col) * Math.max(...row);
}

console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) // 4000
console.log(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) // 120
console.log(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) // 130