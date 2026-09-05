class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2

            count = 0
            d = 1

            for i in weights:
                if mid < i:
                    d = days + 1
                    break

                if count + i <= mid:
                    count += i
                else:
                    count = i
                    d += 1

            if d <= days:
                res = min(mid, res)   # <-- was d
                r = mid - 1
            else:
                l = mid + 1

        return res
                
