class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickSelect(l, r):
            p = l
            pivot  = nums[r]

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p < target:
                return quickSelect(p+1, r)
            elif p > target:
                return quickSelect(l, p-1)
            else:
                 return nums[p]

        return quickSelect(0, len(nums)-1)