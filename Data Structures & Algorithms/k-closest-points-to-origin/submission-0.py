import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap = []
        for x in points:
            dist = math.sqrt((x[0])**2 + (x[1])**2)
            minheap.append([dist, x[0], x[1]])

        heapq.heapify(minheap)
        result = []
        for _ in range(k):
            x = heapq.heappop(minheap)
            result.append([x[1], x[2]])

        return result