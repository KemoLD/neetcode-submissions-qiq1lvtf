class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        visited = {}
        result = 0

        for i in range(len(s)):
            if s[i] in visited:
                left = max(visited[s[i]] + 1, left)


            visited[s[i]] = i
            result = max(result, i - left + 1)

        return result