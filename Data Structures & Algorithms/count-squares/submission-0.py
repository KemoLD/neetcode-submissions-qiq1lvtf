class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point[0], point[1]
        for x,y in self.pts:
            if (abs(x - x1) != abs(y - y1)) or x == x1 or y == y1:
                continue

            res += self.ptsCount[(x, y1)] * self.ptsCount[(x1, y)]
        return res
        
