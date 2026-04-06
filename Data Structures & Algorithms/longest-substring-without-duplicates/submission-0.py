class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxi = 0
        x = set()
        left = 0

        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[left])
                left += 1

            x.add(s[i])
            maxi = max(maxi, i - left + 1)

        return maxi
        