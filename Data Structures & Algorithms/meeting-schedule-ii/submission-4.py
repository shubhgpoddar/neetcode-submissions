"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 1. sort intervals by start time
        # 2. T = 0, push to heap, T = start time, peak and if not, push, T =. start time. Meeting rooms = number of items in the heap

        intervals.sort(key=lambda x:x.start)
        heap = []

        for time in intervals:
            if not heap:
                heapq.heappush(heap, time.end)
            else:
                # meeting room is available
                if time.start >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, time.end)
        return len(heap)
                

            



        