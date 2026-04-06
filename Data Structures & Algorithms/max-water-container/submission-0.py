class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maxi = 0

        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)
            maxi = max(curr, maxi)

            if heights[left] > heights[right]:
                right -=1
            elif heights[left] < heights[right]:
                left += 1
            else:
                if heights[left + 1] > heights[right - 1]:
                    left +=1
                else:
                    right -=1

        return maxi