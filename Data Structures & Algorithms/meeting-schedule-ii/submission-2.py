"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# sweep line algorithm
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = [i.start for i in intervals]
        endTime = [i.end for i in intervals]

        startTime.sort()
        endTime.sort()

        count = 0
        meetingrooms = 0
        start = 0
        end = 0

        while start < len(startTime) and end < len(endTime):
            if startTime[start] < endTime[end]:
                count+=1
                start+=1
            else:
                end+=1
                count-=1
            meetingrooms = max(meetingrooms, count)
        return meetingrooms
            
        