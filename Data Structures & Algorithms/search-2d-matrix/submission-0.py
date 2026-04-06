class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom -= 1
            elif target > matrix[mid][-1]:
                top += 1
            else:
                break

        if not top <= bottom:
            return False

        left = 0
        right = len(matrix[0]) - 1
        row = (top + bottom) // 2

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return False