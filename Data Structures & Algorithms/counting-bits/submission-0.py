class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):

            if i == 2 * offset:
                offset = 2 * offset
            result[i] = 1 + result[i - offset]


        return result