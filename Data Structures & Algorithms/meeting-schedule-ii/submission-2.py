"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = []
        ends = []
        count = 0
        maxRooms = 0

        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)

        left = 0
        right = 0
        starts.sort()
        ends.sort()

        while left < len(intervals):
            if starts[left] < ends[right]:
                count += 1
                left += 1
            else:
                right += 1
                count -= 1
            maxRooms = max(maxRooms, count)

        return maxRooms