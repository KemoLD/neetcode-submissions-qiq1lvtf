class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def capture(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'O':
                return
            board[x][y] = 'T'
            capture(x-1,y)
            capture(x+1,y)
            capture(x,y-1)
            capture(x,y+1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in [0, len(board)-1] or j in [0, len(board[0])-1]:
                    capture(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'