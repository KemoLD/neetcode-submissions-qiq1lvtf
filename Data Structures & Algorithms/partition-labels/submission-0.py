class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0
        end = 0
        endIdx = {}

        for i in range(len(s)):
            endIdx[s[i]] = i

        for i in range(len(s)):
            size += 1
            end = max(endIdx[s[i]], end)

            if i == end:
                res.append(size)
                size = 0

        return res
