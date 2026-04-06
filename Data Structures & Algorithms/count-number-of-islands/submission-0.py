class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count = 0

        def search(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 

            if grid[x][y] != '1' or (x,y) in visited:
                return

            visited.add((x,y))
            search(x+1, y)
            search(x-1, y)
            search(x, y-1)
            search(x, y+1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not (i,j) in visited:
                    count += 1
                    search(i,j)

        return count