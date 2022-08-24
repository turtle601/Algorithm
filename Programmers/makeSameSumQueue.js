// 프로그래머스 두 큐 함 같게 하기
class Queue {
  constructor(queue) {
    this.queue = queue;
    this.front = 0;
    this.rear = queue.length - 1;
  }

  push(value) {
    this.queue[++this.rear] = value; 
  }

  shift() {
    const returnValue = this.queue[this.front];
    this.front += 1;

    return returnValue;
  } 
}

const sum = (arr) => {
  return arr.reduce((pre, cur) => pre + cur, 0);
}


function solution(queue1, queue2) {
  let result = 0;

  let q1Sum = sum(queue1);
  let q2Sum = sum(queue2);

  if ((q1Sum + q2Sum) % 2 !== 0 || result > 600000) {
    return -1;
  }

  const q1 = new Queue(queue1);
  const q2 = new Queue(queue2);

  while(q1Sum !== q2Sum) {
    if (q1Sum <= 0 || q2Sum <= 0){
      return -1;
    }

    if (q1Sum > q2Sum) {
      const popNum = q1.shift();
      q2.push(popNum);
      q1Sum -= popNum;
      q2Sum += popNum;
      
    } else {
      const popNum = q2.shift();
      q1.push(popNum);
      q2Sum -= popNum;
      q1Sum += popNum;
      
    }

    result += 1;
  };

  return result;
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1])) // 2
console.log(solution([1, 2, 1, 2],	[1, 10, 1, 2])) // 7
console.log(solution([1, 1],	[1, 5])) // -1