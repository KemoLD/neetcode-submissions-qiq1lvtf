class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0

            curr += n

            maxi = max(maxi, curr)

        return maxi