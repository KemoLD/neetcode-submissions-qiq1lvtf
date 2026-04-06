class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        res = [False] * (len(s) + 1)
        res[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:

                if res[i] == True:
                    break

                if i + len(word) <= len(s):
                    if s[i : i + len(word)] == word:
                        res[i] = res[i + len(word)]

        return res[0]

