class MinHeap {
  constructor() {
    this.heap = [null];
  }

  _swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  isEmpty() {
    return this.heap.length === 1;
  }

  push(value) {
    this.heap.push(value);

    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor(currentIdx / 2);

    while (parentIdx !== 0 && this.heap[parentIdx] > value) {
      this._swap(currentIdx, parentIdx);

      currentIdx = parentIdx;
      parentIdx = Math.floor(currentIdx / 2);
    }
  }

  shift() {
    if (this.heap.length === 2) return this.heap.pop();

    const returnValue = this.heap[1];
    this.heap[1] = this.heap.pop();

    let currentIdx = 1;
    let leftIdx = 2;
    let rightIdx = 3;

    while (
      this.heap[currentIdx] > this.heap[leftIdx] ||
      this.heap[currentIdx] > this.heap[rightIdx]
    ) {
      if (this.heap[rightIdx] > this.heap[leftIdx]) {
        this._swap(currentIdx, leftIdx);
        currentIdx = leftIdx;
      } else {
        this._swap(currentIdx, rightIdx);
        currentIdx = rightIdx;
      }

      leftIdx = currentIdx * 2;
      rightIdx = currentIdx * 2 + 1;
    }

    return returnValue;
  }
}

function dijkstra(N, road) {
  const priorityQueue = new MinHeap();
  const dist = new Array(N + 1).fill(Infinity);

  dist[1] = 0; // 시작점

  priorityQueue.push({ node: 1, cost: 0 });

  while (!priorityQueue.isEmpty()) {
    const { node: current, cost: currentCost } = priorityQueue.shift();

    for (const [start, end, cost] of road) {
      const nextCost = currentCost + cost;

      if (start === current && nextCost < dist[end]) {
        dist[end] = nextCost;
        priorityQueue.push({ node: end, cost: nextCost });
      } else if (end === current && nextCost < dist[start]) {
        dist[start] = nextCost;
        priorityQueue.push({ node: start, cost: nextCost });
      }
    }
  }

  return dist;
}

function solution(N, road, K) {
  const dist = dijkstra(N, road);
  return dist.filter((v) => v <= K).length;
}

console.log(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  )
);
console.log(
  solution(
    6,
    [
      [1, 2, 1],
      [1, 3, 2],
      [2, 3, 2],
      [3, 4, 3],
      [3, 5, 2],
      [3, 5, 3],
      [5, 6, 1],
    ],
    4
  )
);
