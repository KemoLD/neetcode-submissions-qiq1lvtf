class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n+1)
        res[0] = 0
        prefix = 1

        for i in range(1, n + 1):
            if i == prefix * 2:
                prefix = i
            
            res[i] = 1 + res[i - prefix]

        return res
