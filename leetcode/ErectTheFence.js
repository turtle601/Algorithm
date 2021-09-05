// leetcode 587 ErectTheFence

// Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
// Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

/**
 * 
 * @param {number[][]} p1 
 * @param {number[][]} p2 
 * @param {number[][]} p3 
 * @returns {number}
 */
// ccw 알고리즘 함수
function ccw(p1, p2, p3){
    // 외적을 구하는 함수 - 외적을 통해 해당 선분이 어떤 방향으로 돌아가고 있는지 판단
    // 음수 : 시계 방향
    // 0 : 직성
    // 양수 : 반시계 방향
    return (p3[1] - p2[1])*(p2[0]-p1[0]) - (p2[1]-p1[1])*(p3[0]-p2[0]);
}

/**
 * @param {number[][]} trees
 * @return {number[][]}
 */
const outerTrees = function(trees) {
    
    // 정렬
    trees.sort((a,b) => (a[0] - b[0]) || (a[1] - b[1]));
    
    let upper = [];
    let lower = [];

    for (let t of trees){
        // upper는 반시계 방향일 때만 가져온다. -> 시계방향( ccw < 0 )일 경우 pop()
        while (upper.length >= 2 && ccw(upper[upper.length - 2], upper[upper.length-1], t) < 0){
            upper.pop();
        }
        // lower는 시계 방향일 때만 가져 온다. => 반시걔 방향 ( ccw > 0) 일 경우 pop()
        while (lower.length >= 2 && ccw(lower[lower.length -2], lower[lower.length-1], t) > 0){
            lower.pop();
        }
        upper.push(t);
        lower.push(t);
    }
    return [...new Set([...upper,...lower])];
};

// execute
const trees = [[0,0],[0,100],[100,100],[100,0],[50,50]];
const trees1 = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]];
console.log(outerTrees(trees1));