class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visit = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i, j))


        def add(x , y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x,y) in visit or grid[x][y] == -1:
                return
            
            q.append([x,y])
            visit.add((x, y))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist

                add(i + 1, j)
                add(i - 1, j)
                add(i, j + 1)
                add(i, j - 1)
            dist += 1