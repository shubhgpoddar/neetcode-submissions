"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:[x.start])
        occupied = []

        for mtg in intervals:
            if occupied and mtg.start >= occupied[0]:
                heapq.heappop(occupied)   
            heapq.heappush(occupied, mtg.end)
        return len(occupied)


        