class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []

        def search(i):
            if i >= len(s):
                res.append(partitions.copy())
                return

            for j in range(i, len(s)):
                if isPal(i, j):
                    partitions.append(s[i: j + 1])
                    search(j + 1)
                    partitions.pop()

        def isPal(x, y):
            while x < y:
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True

        search(0)
        return res