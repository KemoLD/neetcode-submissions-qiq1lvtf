class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        seen = set()
        seen.add(0)
        target = sum(nums) // 2

        for x in nums:
            temp = seen.copy()
            for y in seen:
                if x + y == target:
                    return True
                temp.add(x + y)
            seen = temp

        return False
