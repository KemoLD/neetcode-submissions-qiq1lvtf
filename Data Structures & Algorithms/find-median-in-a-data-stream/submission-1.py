class MedianFinder:

    def __init__(self):
        self.small = [] # small = max heap (negatives)
        self.large = [] # large = min heap (positives)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) # push to max heap

        # Balance largest of small into large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Maintain size property
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

        
        