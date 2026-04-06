class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)

            if l > window[0]:
                window.popleft()

            if r + 1 >= k:
                result.append(nums[window[0]])
                l += 1
            r += 1

        return result