class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [ [grid[0][0],0,0] ]
        visit = set()
        directions = [ [1,0], [-1,0], [0,1], [0,-1] ]

        visit.add((0,0))
        while minHeap:
            t, x, y = heapq.heappop(minHeap)
            if x == N - 1 and y == N - 1:
                return t

            for xpos, ypos in directions:
                newX, newY = x + xpos, y + ypos
                if newX < 0 or newY < 0 or newX >= N or newY >= N or (newX, newY) in visit:
                    continue
                heapq.heappush(minHeap, [max(t, grid[newX][newY]), newX, newY])
                visit.add((newX, newY))