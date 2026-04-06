class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        seen = set()
        seen.add(0)
        target = sum(nums) // 2

        for x in nums:
            temp = set()
            for num in seen:
                if x + num == target:
                    return True
                temp.add(x + num)
                temp.add(num)
            seen = temp

        return False
            