class MinHeap {
  constructor() {
    this.heap = [null];
  }

  swap(idx1, idx2) {
    const temp = this.heap[idx1];
    this.heap[idx1] = this.heap[idx2];
    this.heap[idx2] = temp;
  }

  push(value) {
    this.heap.push(value);
    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor(currentIdx / 2);

    while (parentIdx !== 0 && this.heap[parentIdx] > value) {
      this.swap(parentIdx, currentIdx);

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
      this.heap[currentIdx > this.heap[rightIdx]]
    ) {
      if (this.heap[rightIdx] < this.heap[leftIdx]) {
        this.swap(currentIdx, rightIdx);

        currentIdx = rightIdx;
      } else {
        this.swap(currentIdx, leftIdx);

        currentIdx = leftIdx;
      }

      leftIdx = currentIdx * 2;
      rightIdx = currentIdx + 2 + 1;
    }

    return returnValue;
  }
}
