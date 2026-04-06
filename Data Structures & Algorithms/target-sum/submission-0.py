class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def backtrack(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            if (i,curr) in cache:
                return cache[(i, curr)]

            cache[(i, curr)] = backtrack(i+ 1, curr + nums[i]) + backtrack(i+ 1, curr - nums[i])
            return cache[(i, curr)]

        return backtrack(0,0)