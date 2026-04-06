class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text2) < len(text1):
            text1, text2 = text2, text1

        prev = [0 for _ in range(len(text1) + 1)]
        curr = [0 for _ in range(len(text1) + 1)]

        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(prev[j], curr[j+1])
            prev, curr = curr, prev

        return prev[0]
        