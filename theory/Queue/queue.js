function Queue(array) {
  this.array = array ? array : [];
  this.tail = array ? array.length : 0;
  this.head = 0;
}

Queue.prototype.enqueue = function () {
  return (this.array[this.tail++] = element);
};

Queue.prototype.dequeue = function () {
  if (this.tail === this.head) return undefined;

  let element = this.array[this.head];
  delete this.array[this.head];

  return element;
};

let queue = new Queue([1, 2]);
console.log(queue);

queue.enqueue(3);
queue.enqueue(4);

console.log(queue);

console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());
