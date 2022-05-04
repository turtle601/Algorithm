function Node(data) {
  this.data = data;
  this.next = null;
  this.tail = null;
}

function DoubleLinkedList() {
  this.head = null;
  this.tail = null;
  this.length = 0;
}

DoubleLinkedList.prototype.size = function () {
  return this.length;
};

DoubleLinkedList.prototype.isEmpty = function () {
  return this.length === 0;
};

DoubleLinkedList.prototype.printNode = function () {
  process.stdout.write("head -> ");
  for (let node = this.head; node != null; node = node.next) {
    process.stdout.write(`${node.data} -> `);
  }
  console.log("null");
};

DoubleLinkedList.prototype.printNodeInverse = function () {
  let temp = [];

  process.stdout.write("null <- ");

  for (let node = this.tail; node != null; node.prev) {
    temp.push(node.data);
  }
  for (let node = temp.length - 1; i > -1; i--) {
    process.stdout.write(`${temp[i]} <- `);
  }
  console.log("null");
};

DoubleLinkedList.prototype.append = function (value) {
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

DoubleLinkedList.prototype.insert = function (value, position = 0) {
  // 가능한 position 위치인지
  if (position < 0 || position > this.length) {
    return false;
  }

  let node = new Node(value);

  let current = this.head;
  let prev = null;

  // 제일 앞에 넣을 때
  if (position === 0) {
    // head에 아무것도 없을 때
    if (this.head === null) {
      this.head = node;
      this.tail = node;
    } else {
      current.prev = node;
      node.next = current;
      this.head = node;
    }

    // 제일 마지막에 넣을 때
  } else if (position === this.length) {
    current = this.tail;
    current.next = node;
    node.prev = current;
    this.tail = node;

    // 중간에 넣을 때
  } else {
    for (let idx = 0; idx < position; idx++) {
      prev = current;
      current = current.next;
    }

    prev.next = node;
    node.prev = prev;

    node.next = current;
    current.prev = node;
  }

  this.length++;

  return true;
};

DoubleLinkedList.prototype.remove = function (value) {
  let current = this.head;
  let prev = null;

  for (let i = 0; i < this.length; i++) {
    if (current.data === value) {
      break;
    }
    prev = current;
    current = current.next;
  }

  if (current.data !== value) {
    return null;
  }

  // 제일 앞에 것 삭제
  if (current === this.head) {
    this.head = current.next;
    if (this.length === 1) this.tail = null;
    else this.head.prev = null;
    // 제일 마지막 것 삭제
  } else if (current === this.tail) {
    this.tail = current.prev;
    this.tail.next = null;
    // 중간에 것 삭제
  } else {
    prev.next = current.next;
    current.next.prev = prev;
  }

  this.length--;
};

DoubleLinkedList.prototype.removeAt = function (position = 0) {
  let current = this.head;
  let prev = null;

  // 1. 가능한 포지션 찾기
  if (position < 0 || position > this.length - 1) {
    return false;
  }

  // 첫번째 요소를 삭제
  if (current === this.head) {
    this.head = current.next;
    if (this.length === 1) this.tail = null;
    else this.head.prev = null;
    // 마지막 요소를 삭제
  } else if (current === this.tail) {
    current.prev = this.tail;
    this.tail.next = null;
    // 중간 요소를 삭제
  } else {
    for (let i = 0; i < position; i++) {
      prev = current;
      current = current.next;
    }

    prev.next = current.next;
    current.next.prev = prev;
  }

  this.length--;

  return true;
};

const dll = new DoubleLinkedList();

dll.insert(1);
dll.insert(100);
dll.insert(10000);

dll.printNode();

dll.remove(100);

dll.printNode();

dll.remove(1);

dll.printNode();
