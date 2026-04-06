class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [ -x for x in count.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

           
            if heap:
                x =  x = heapq.heappop(heap)
                if x and 1 + x != 0:
                    q.append([1 + x , n + time])

            if q and q[0][1] <= time:
                y = q.popleft()
                heapq.heappush(heap, y[0])

        return time

            