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
    let answer = 0;
    let depth;
    // visited = [false] * len(nums);
    // new Array(nums.length).fill(false) => 이건 시간 복잡도가 오래 걸림
    let visited;
    (visited = []).length = nums.length;
    visited.fill(false);

    const bfs = (k) => {
        while (!visited[k]){
            depth += 1;
            visited[k] = true;
            k = nums[k];
        }
    }
    
    nums.forEach((val, idx) => {
        depth = 0;
        bfs(idx);
        answer = (depth >= answer) ? depth : answer; 
    })

    return answer;
};

// execute
const nums = [5,4,0,3,1,6,2];
console.log(arrayNesting(nums));