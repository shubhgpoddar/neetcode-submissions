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
        i = 0
        j = i + 1

        while i < len(intervals) and j < len(intervals) and i < j:
            if intervals[i].end > intervals[j].start:
                return False
            i+=1
            j+=1
        return True

        

