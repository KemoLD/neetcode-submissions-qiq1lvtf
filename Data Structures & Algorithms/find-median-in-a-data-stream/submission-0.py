import heapq

class MedianFinder:

    def __init__(self):
        # small = max heap (negatives)
        # large = min heap (positives)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # push to max heap
        heapq.heappush(self.small, -num)

        # ensure ordering: max(small) <= min(large)
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

        