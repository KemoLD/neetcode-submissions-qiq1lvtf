class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            currSum = 0
            subarrays = 1
            for x in nums:
                currSum += x
                if currSum > largest:
                    subarrays += 1
                    currSum = x

            return subarrays <= k

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = (l + r) //2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
