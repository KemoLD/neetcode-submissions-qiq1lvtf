class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, array):
            if i >= len(array):
                res.append(array.copy())
                return

            for x in range(i, len(array)):
                array[i], array[x] = array[x], array[i]
                backtrack(i + 1, array)
                array[i], array[x] = array[x], array[i]

        backtrack(0, nums)
        return res

