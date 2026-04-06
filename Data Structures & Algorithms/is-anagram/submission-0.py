class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        one = ''.join(sorted(s))
        two = ''.join(sorted(t))

        return one == two
        