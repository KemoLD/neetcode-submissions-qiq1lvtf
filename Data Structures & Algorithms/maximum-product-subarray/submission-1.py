class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        currMin = 1
        currMax = 1

        for n in nums:

            tmp = currMin
            currMin = min(n, n * tmp, n * currMax)
            currMax = max(n, n * tmp, n * currMax)
            res = max(res, currMax)

        return res

