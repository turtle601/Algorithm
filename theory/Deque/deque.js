function Node(data) {
  this.data = data;
  this.next = null;
  this.prev = null;
}

function Deque() {
  this.head = null;
  this.tail = null;
  this.length = 0;
}

Deque.prototype.size = function () {
  return this.length;
};

Deque.prototype.isEmpty = function () {
  return this.length === 0;
};

Deque.prototype.printNode = function () {
  process.stdout.write("head -> ");
  for (let node = this.head; node != null; node = node.next) {
    process.stdout.write(`${node.data} -> `);
  }
  console.log("null");
};

Deque.prototype.printNodeInverse = function () {
  let temp = [];
  process.stdout.write("null <- ");

  for (let node = this.tail; node != null; node = node.prev) {
    temp.push(node.data);
  }
  for (let node = temp.length - 1; i > -1; i--) {
    process.stdout.write(`${temp[i]} <- `);
  }
  console.log("null");
};

Deque.prototype.pushFront = function (value) {
  let node = new Node(value);

  if (this.head === null) {
    this.head = node;
    this.tail = node;
  } else {
    this.head.prev = node;
    node.next = this.head;
    this.head = node;
  }
};

Deque.prototype.popFront = function () {
  if (this.head === null) {
    return false;
  }

  const data = this.head.data;

  this.head.prev = null;
  this.head = this.head.next;
  this.length--;

  return data;
};

Deque.prototype.push = function (value) {
  let node = new Node(value);

  if (this.head === null) {
    this.head = node;
    this.tail = node;
  } else {
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = node;
  }
};

Deque.prototype.pop = function () {
  if (this.head === null) {
    return false;
  }

  const data = this.tail;
  let current = this.tail;

  current.prev.next = null;
  this.tail = current.prev;

  this.length--;

  return data;
};

const deque = new Deque();
// test code
deque.push(1);
deque.printNode();

deque.push(2);
deque.printNode();

deque.push(3);
deque.printNode();

deque.pop();
deque.printNode();

deque.pushFront(4);
deque.printNode();

deque.popFront();
deque.printNode();
