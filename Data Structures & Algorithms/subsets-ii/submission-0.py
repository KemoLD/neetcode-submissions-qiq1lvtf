class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def search(index, curr):
            if index >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            search(index + 1, curr)

            curr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            search(index + 1, curr)

        search(0, [])
        return res
