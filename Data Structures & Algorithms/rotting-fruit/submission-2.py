class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        def search(x,y):
            nonlocal fresh
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0  or grid[x][y] == 2:
                return

            grid[x][y] = 2
            fresh -= 1
            q.append((x, y))

        while q and fresh:
            for _ in range(len(q)):
                i, j = q.popleft()

                search(i + 1, j)
                search(i - 1, j)
                search(i, j - 1)
                search(i, j + 1)

            result += 1

        return result if fresh == 0 else -1


