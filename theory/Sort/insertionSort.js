function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    const choice = array[i];
    let j = i - 1;

    while (j > -1 && choice < array[j]) {
      array[j + 1] = array[j];
      j--;
    }

    array[j + 1] = choice;
  }

  return array;
}

const a = insertionSort([5, 6, 1, 2, 4, 3]); // [1, 2, 3, 4, 5, 6]

console.log(a);
