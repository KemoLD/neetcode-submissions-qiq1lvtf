class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in count:
                return [count[x], i]
            else:
                count[nums[i]] = i

        return -1
        