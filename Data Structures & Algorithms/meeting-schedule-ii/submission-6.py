"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        occupied = []
        for interval in intervals:
            if not occupied:
                heapq.heappush(occupied, interval.end)
            else:
                if occupied[0] > interval.start:
                    heapq.heappush(occupied, interval.end)
                else:
                    heapq.heappop(occupied)
                    heapq.heappush(occupied, interval.end)
        return len(occupied)


        