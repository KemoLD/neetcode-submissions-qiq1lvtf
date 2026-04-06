from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for x in nums:
            if not res or (res and res[-1] < x):
                res.append(x)
                continue

            idx = bisect_left(res, x)
            res[idx] = x

        return len(res)