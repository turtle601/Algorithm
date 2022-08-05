// 프로그래머스 베스트 앨범

const map = new Map();
const sum = new Map();

function solution(genres, plays) {
  const n = genres.length;

  for (let i = 0; i < n; i++) {
    const genre = map.get(genres[i]);
    map.set(genres[i], genre ? [...genre, [i, plays[i]]] : [[i, plays[i]]]);
  }

  for (const [key, value] of map) {
    sum.set(
      key,
      value.reduce((pre, cur) => pre + cur[1], 0)
    );
    value.sort((x, y) => y[1] - x[1] || x[0] - y[0]);
  }

  const sortingSum = [...sum].sort((x, y) => y[1] - x[1]);

  let result = [];

  for (const [key, _] of sortingSum) {
    const genreMap = map.get(key);

    for (let i = 0; i < genreMap.length; i++) {
      if (i === 2) break;
      result.push(genreMap[i][0]);
    }
  }

  return result;
}
