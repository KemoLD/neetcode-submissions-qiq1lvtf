class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def kSum(k, index, target):
            if k != 2:
                for i in range(index, len(nums) - k + 1):
                    if i > index and nums[i] == nums[i-1]:
                        continue
                    curr.append(nums[i])
                    kSum(k-1, i + 1, target - nums[i])
                    curr.pop()
                return

            left = index
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]] + curr.copy())
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        kSum(4, 0, target)
        return res