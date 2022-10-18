function convert_iter(num, base) {
  let str = "";
  while(num){
      str = String(num % base) + str;
      num = parseInt(num / base);
  }
  return str;
}

function convert_124(num){
  let answer = "";
  
  while(num){
      if (num % 3 === 0){
          answer = "4" + answer; 
          num = parseInt(num / 3) - 1;
      } else {
          answer = String(num % 3) + answer;
          num = parseInt(num / 3);
      }
  } 
  
  return answer;
}

function solution(n) {
  return convert_124(n);
}