const swap = (array, left, right) => {
  const temp = array[left];
  array[left] = array[right];
  array[right] = temp;
};

const partition = function (array, low, high, pivotIndex) {
  // 정렬하는 부분
  const pivot = array[pivotIndex];

  while (low <= high) {
    // 왼쪽, 오른쪽 수를 규칙과 비교해 다음 수로 넘어갑니다.
    while (array[low] < pivot) low++;
    while (array[high] > pivot) high--;
    if (low <= high) {
      // 왼쪽이 기준보다 크고, 오른쪽이 기준보다 작으면
      swap(array, low, high);
      low++;
      high--;
    }
  }

  swap(array, high, pivotIndex); // 마지막으로 기준과 만난 수를 바꿔준다.

  return high;
};

const quickSort = function (array, left, right) {
  // 재귀하는 부분
  if (!left) left = 0;
  if (!right) right = array.length - 1;
  let pivotIndex = left; // 배열 가장 오른쪽의 수를 기준으로 뽑습니다.
  pivotIndex = partition(array, left + 1, right, pivotIndex); // right - 1을 하는 이유는 기준(현재 right)을 제외하고 정렬하기 위함입니다.
  if (left < pivotIndex - 1) quickSort(array, left, pivotIndex - 1); // 기준 왼쪽 부분 재귀
  if (pivotIndex + 1 < right) quickSort(array, pivotIndex + 1, right); // 기준 오른쪽 부분 재귀
  return array;
};

const a = quickSort([4, 1, 7, 6, 3, 8, 2, 5]); // [1,2,3,4,5,6,7,8]

console.log(a);
