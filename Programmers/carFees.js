function solution(fees, records) {
  const [defaultTime, defaultPrice, moreTime, morePrice] = fees;
  const carMap = new Map();
  const timeMap = new Map();

  for (const record of records) {
    recordTime(record, carMap, timeMap);
  }

  // 남은 차량이 존재한다면 모두 제거
  for (const [carNumber, carTimeObj] of carMap) {
    const defaultTime = timeMap.get(carNumber);
    if (carTimeObj !== null) {
      timeMap.set(
        carNumber,
        defaultTime + getTimeDiffer(carTimeObj.inTime, "23:59")
      );
    }
  }

  const result = [];

  for (const [carNumber, carTime] of timeMap) {
    if (carTime <= defaultTime) {
      result.push([carNumber, defaultPrice]);
    } else {
      const price =
        defaultPrice +
        Math.ceil((carTime - defaultTime) / moreTime) * morePrice;
      result.push([carNumber, price]);
    }
  }

  return result.sort((x, y) => x[0] - y[0]).map((v) => v[1]);
}

function recordTime(record, carMap, timeMap) {
  const [time, carNumber, active] = record.split(" ");

  const defualtCar = carMap.get(carNumber) || null;
  const defaultTime = timeMap.get(carNumber) || 0;

  if (defualtCar === null) {
    timeMap.set(carNumber, defaultTime);
    carMap.set(carNumber, {
      inTime: time,
    });
  } else {
    const { inTime } = defualtCar;
    const sumTime = timeMap.get(carNumber);

    timeMap.set(carNumber, sumTime + getTimeDiffer(inTime, time));
    carMap.set(carNumber, null);
  }
}

function getTimeDiffer(inTime, outTime) {
  const [inHour, inMin] = inTime.split(":");
  const [outHour, outMin] = outTime.split(":");

  inTime = +inHour * 60 + +inMin;
  outTime = +outHour * 60 + +outMin;

  return outTime - inTime;
}

console.log(
  solution(
    [180, 5000, 10, 600],
    [
      "05:34 5961 IN",
      "06:00 0000 IN",
      "06:34 0000 OUT",
      "07:59 5961 OUT",
      "07:59 0148 IN",
      "18:59 0000 IN",
      "19:09 0148 OUT",
      "22:59 5961 IN",
      "23:00 5961 OUT",
    ]
  )
);
console.log(
  solution(
    [120, 0, 60, 591],
    [
      "16:00 3961 IN",
      "16:00 0202 IN",
      "18:00 3961 OUT",
      "18:00 0202 OUT",
      "23:58 3961 IN",
    ]
  )
);
console.log(solution([1, 461, 1, 10], ["00:00 1234 IN"]));
