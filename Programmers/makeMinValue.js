function solution(A,B){
  const n = A.length;
  
  A = A.sort((x,y) => x - y);
  B = B.sort((x,y) => y - x);
  
  let result = 0;
  
  for (let i = 0; i < A.length; i++){
      result += A[i] * B[i];
  }
  
  return result;
}