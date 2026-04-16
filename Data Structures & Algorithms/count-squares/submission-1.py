class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        for (x, y) in self.ptsCount:
            if abs(x - x1) != abs(y - y1) or x == x1 or y == y1:
                continue

            res += (
                self.ptsCount[(x, y)] *
                self.ptsCount.get((x, y1), 0) *
                self.ptsCount.get((x1, y), 0)
            )

        return res
        
