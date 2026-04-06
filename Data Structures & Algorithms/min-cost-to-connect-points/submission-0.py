class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minHeap = [[0,0]]
        while len(visit) < len(points):
            dist, p = heapq.heappop(minHeap)
            if p in visit:
                continue

            res += dist
            visit.add(p)
            for i,j in adj[p]:
                if j not in visit:
                    heapq.heappush(minHeap, [i, j])

        return res