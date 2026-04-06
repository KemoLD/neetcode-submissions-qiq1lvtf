class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if abs(first) > abs(second):
                heapq.heappush(heap, -(abs(first) - abs(second)) )

        return abs(heap[0]) if heap else 0