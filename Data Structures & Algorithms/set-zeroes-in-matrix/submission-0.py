class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            if rows[i] == True:
                for j in range(len(matrix[0])):
                    matrix[i][j] = '0'

        for i in range(len(matrix[0])):
            if cols[i] == True:
                for j in range(len(matrix)):
                    matrix[j][i] = '0'