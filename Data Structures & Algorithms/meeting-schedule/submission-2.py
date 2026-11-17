"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        heap = []

        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                if heap[0] > interval.start:
                    return False
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, interval.end)

        return True



