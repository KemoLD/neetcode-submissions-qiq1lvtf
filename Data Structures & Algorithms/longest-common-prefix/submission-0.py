class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            j = 0

            while j < min(len(prefix), len(s)) and prefix[:j+1] == s[:j+1]:
                j += 1

            prefix = prefix[:j]

        return prefix
            