def solution(arr):
  n = len(arr)

  def recur(depth):
    
    if depth == 3:
      print(arr)
      return
    
    for i in range(depth, n):
      arr[i], arr[depth] = arr[depth], arr[i]
      recur(depth + 1)
      arr[i], arr[depth] = arr[depth], arr[i]    

  recur(0)

solution([1,2,3])
