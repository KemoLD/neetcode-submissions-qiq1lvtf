class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)
        before = 1
        after = 1

        for i in range(len(nums)):
            result[i] = before * result[i]
            before = before * nums[i]

        for i in range(len(nums)-1, -1, -1):
            result[i] = after * result[i]
            after = after * nums[i]

        return result
        