function Node(data) {
  this.data = data;
  this.next = null;
}

function LinkList() {
  this.head = null;
  this.length = 0;

  this.isSize = () => this.length;
  this.isEmpty = () => this.length === 0;
  this.printNode = () => {
    for (let node = this.head; node != null; node = node.next) {
      process.stdout.write(`${node.data} -> `);
    }

    console.log("null");
  };

  this.insert = (value, position = 0) => {
    const node = new Node(value);

    let current = this.head;
    let prev = null;

    // 삽입 가능한 길이인지 체크
    if (position < 0 || position >= this.length) {
      return false;
    }

    if (position === 0) {
      node.next = current;
      this.head = node;
    } else {
      for (let idx = 0; idx < position; idx++) {
        prev = current;
        current = current.next;
      }

      prev.next = node;
      node.next = current;
    }
    this.length++;
    return true;
  };

  this.remove = (value) => {
    let current = this.head;
    let prev = null;

    for (current; current.next != null; current = current.next) {
      prev = current;
      if (current.data === value) {
        break;
      }
    }

    if (current.data !== value) {
      return null;
    }

    if (current === this.head) {
      this.head = current.next;
    } else {
      prev.next = current.next;
    }

    this.length--;
  };

  this.removeAt = (position = 0) => {
    let current = this.head;
    let prev = null;

    // 정확한 입력값인지 확인
    if (position < 0 || position >= this.length) {
      return false;
    }

    for (let idx = 0; idx < position; idx++) {
      prev = current;
      current = current.next;
    }

    if (position === 0) {
      this.head = current.next;
    } else {
      prev.next = current.next;
    }

    this.length--;

    return true;
  };

  this.indexOf = (value) => {
    let current = this.head;

    for (let idx = 0; idx < this.length; idx++) {
      if (current.data === value) {
        return idx;
      }
      current = current.next;
    }

    return null;
  };

  this.append = (data) => {
    const node = new Node(data);
    let current = this.head;

    if (current === null) {
      this.head = node;
    } else {
      while (current.next != null) {
        current = current.next;
      }
      current.next = node;
    }

    this.length++;
  };
}

const li = new LinkList();
// 연결리스트 출력
li.printNode();

// 삽입 1
li.append(123);
li.printNode();

// 삽입 2
li.append(456);
li.printNode();

// 첫번째 위치 삽입
li.insert(789, 1);
li.printNode();

// 2번째 위치 삽입
li.insert(222, 2);
li.printNode();

// 위치 찾기 연산
console.log(li.indexOf(222));
console.log(li.indexOf(789));

// 위치 삭제 연산
li.removeAt(1);
li.printNode();

li.removeAt(2);
li.printNode();

// // 삭제 연산
// li.remove(123);
// li.printNode();

// // 삭제 연산
// li.remove(789);
// li.printNode();
