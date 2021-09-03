// leetcode 565. Array Nesting

// Example
// Input: nums = [5,4,0,3,1,6,2]
// Output: 4
// Explanation: 
// nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
// One of the longest sets s[k]:
// s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

'use strict'

/**
 * @param {number[]} nums
 * @return {number}
 */
const arrayNesting = function(nums) {
    let answer = 0;  // 최종 정답
    let set = new Set();
    let count;  // 순회 깊이를 나타내는 변수

    // 해당 idx에 해당하는 값 탐색해보는 함수
    const dfs = (k) => {
        if(set.has(k)){
            return  
        } else {
            set.add(k);
            count += 1;
            dfs(nums[k]);
            return;
        }
    }

    // idx별로 dfs탐색 
    nums.forEach((val, idx) => {
        count = 0;
        dfs(idx);
        answer = (count >= answer) ? count : answer;
    })

    return answer;
};

// execute
const nums = [5,4,0,3,1,6,2];
console.log(arrayNesting(nums));