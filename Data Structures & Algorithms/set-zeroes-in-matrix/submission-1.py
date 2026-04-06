class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                        matrix[0][j] = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0


        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(1, rows):
                matrix[i][0] = 0

        if rowZero == True:
            for j in range(cols):
                    matrix[0][j] = 0

        
