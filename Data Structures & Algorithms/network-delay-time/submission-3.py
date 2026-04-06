class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]  # (time, node)
        visit = set()
        result = 0

        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            result = max(result, w)

            for nei, wt in edges[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (w + wt, nei))

        return result if len(visit) == n else -1