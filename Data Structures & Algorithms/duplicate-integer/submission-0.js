class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
     hasDuplicate(nums) {
        return new Set(nums).size !== nums.length ;
    }
    
        
}
const myNums = [1, 2, 3, 1];
const sol  = new Solution();
console.log(sol.hasDuplicate(myNums));