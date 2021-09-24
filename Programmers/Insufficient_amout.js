// 프로그래머스 위클리 챌린지 1주차
// 제목 : 부족한 금액 계산하기

'use strict'

function solution(price, money, count) {
    let total = 0;

    for (let cnt = 1; cnt <= count; cnt++ ){
        total += (cnt * price)
    }

    return (total > money) ? total - money : 0;
}

