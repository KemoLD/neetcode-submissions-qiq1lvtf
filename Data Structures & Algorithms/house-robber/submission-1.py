class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
            
        x = [0] * len(nums)
        x[0] = nums[0]
        x[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            x[i] = max( nums[i] + x[i-2], x[i-1])

        return x[len(nums)-1]