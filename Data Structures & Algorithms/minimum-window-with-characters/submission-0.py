class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        res = ""
        resLen = float("inf")
        window = {}
        countT = {}
        for x in t:
            countT[x] = countT.get(x, 0) + 1

        l = 0
        have = 0
        need = len(countT)
        for r in range(len(s)):
            x = s[r]
            window[x] = window.get(x, 0) + 1

            if x in countT and window[x] == countT[x]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res

                