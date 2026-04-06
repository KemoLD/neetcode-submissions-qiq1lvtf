"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])


        left = 0
        right = 0
        count = 0
        maxi = 0

        while left < len(intervals):
            if start[left] < end[right]:
                count += 1
                left += 1
            else:
                count -= 1
                right += 1

            maxi = max(count, maxi)

        return maxi


