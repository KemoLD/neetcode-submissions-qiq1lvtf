class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(x, y, index, visited):

            if index >= len(word):
                return True

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index] or (x,y) in visited:
                return False

            visited.add((x,y))
            return search(x+1, y, index+1, visited) or search(x-1, y, index+1, visited) or search(x, y-1, index+1, visited) or search(x, y+1, index+1, visited)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0, set()):
                    return True

        return False
