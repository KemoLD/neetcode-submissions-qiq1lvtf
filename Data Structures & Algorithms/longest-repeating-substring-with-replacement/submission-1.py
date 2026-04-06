class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        maxF = 0


        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxF = max(maxF, count[s[i]])

            while (i - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, i - left + 1)

        return result