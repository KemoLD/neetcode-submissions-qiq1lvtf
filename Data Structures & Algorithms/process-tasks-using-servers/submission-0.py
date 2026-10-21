class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = [0] * len(tasks)
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            if not available:
                time = busy[0][0]

            while busy and busy[0][0] <= time:
                _, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)
            result[i] = index
            heapq.heappush(busy, (time + duration, weight, index))

        return result