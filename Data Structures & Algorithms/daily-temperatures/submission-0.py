class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i,t = stack.pop()
                res[i] = index - i
            stack.append([index, temp])

        return res
