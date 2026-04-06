class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        let x = new Set(nums)

        return x.size != nums.length

    }
}
