/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let n = nums.length;
    let ans = [];
    for (let i = 0; i < n; i++) {
        ans[i] = nums[i];
    }
    let k = 0;
    for (let j = k + n; j < 2 * n; j++) {
        ans[j] = nums[k];
        ++k;
    }
    return ans;
};