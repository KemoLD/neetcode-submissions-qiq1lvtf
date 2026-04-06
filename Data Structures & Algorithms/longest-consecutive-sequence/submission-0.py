class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxi = 0
        s = set(nums)

        for i in s:
            if i-1 not in s:
                count = 1
                x = i
                while x + 1 in s:
                    count += 1
                    x += 1
                maxi = max(maxi, count)

        return maxi
        