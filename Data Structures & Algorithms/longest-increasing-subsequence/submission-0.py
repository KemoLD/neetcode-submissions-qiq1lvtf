class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        res = [1] * len(nums)
        result = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], 1 + res[j])

            result = max(result, res[i])

        return result