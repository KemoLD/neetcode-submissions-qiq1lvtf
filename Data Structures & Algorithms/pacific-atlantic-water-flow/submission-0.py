class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []

        def search(x, y, prev, ocean):
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]):
                return

            if (x, y) in ocean or heights[x][y] < prev:
                return

            ocean.add((x,y))
            search(x+1, y, heights[x][y], ocean)
            search(x-1, y, heights[x][y], ocean)
            search(x, y+1, heights[x][y], ocean)
            search(x, y-1, heights[x][y], ocean)
        

        for i in range(len(heights)):
            search(i, 0, 0, pacific)
            search(i, len(heights[0]) - 1, 0, atlantic)

        for i in range(len(heights[0])):
            search(0, i, 0, pacific)
            search(len(heights) - 1, i, 0, atlantic)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atlantic and (i,j) in pacific:
                    res.append([i,j])

        return res

        