class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                x, y = stack.pop()
                result = max(result, y * (i - x))
                start = x
            stack.append((start, h))

        for x,y in stack:
            result = max(result, y * (len(heights) - x ))
        return result
            
            