class Solution:
    def reorganizeString(self, s: str) -> str:
        x = Counter(s)
        heap = [ [-count,letter] for letter,count in x.items() ]
        heapq.heapify(heap)

        prev = None
        res = ''
        while heap or prev:
            if prev and not heap:
                return ''

            cnt, l = heapq.heappop(heap)
            cnt += 1
            res += l

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt < 0:
                prev = [cnt, l]


        return res