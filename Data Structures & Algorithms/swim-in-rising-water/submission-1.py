class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [ [grid[0][0],0,0] ]
        res = float('inf')
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        while minHeap:
            i, x, y = heapq.heappop(minHeap)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return i

            if (x, y) in visit:
                continue

            visit.add((x, y))
            for a,b in directions:
                n, m = x + a, y+b
                if n < 0 or n >= len(grid) or m < 0 or m >= len(grid[0]) or (n,m) in visit:
                    continue
                heapq.heappush(minHeap, [max(i, grid[n][m]), n, m])

