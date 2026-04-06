class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for x in hand:
            count[x] = count.get(x, 0) + 1
        
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            x = heap[0]
            for i in range(x, x + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True
