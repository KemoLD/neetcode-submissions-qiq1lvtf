class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use each number as an index, and flip the number at that index to negative. If it's already negative, we've found a duplicate!

        for x in nums:
            #gets the positive value of x. - 1 converts the number into a zero-based array index.
            idx = abs(x) - 1
            if nums[idx] < 0:
                return abs(x)
            nums[idx] = -nums[idx]