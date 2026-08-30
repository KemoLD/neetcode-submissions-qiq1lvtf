class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for x in nums:
            if count == 0:
                res = x
            if res == x:
                count += 1
            else:
                count -= 1

        return res