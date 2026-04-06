class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        one = {}
        two = {}

        for i in range(len(s)):
            one[s[i]] = one.get(s[i], 0) + 1
            two[t[i]] = two.get(t[i], 0) + 1

        return one == two

        