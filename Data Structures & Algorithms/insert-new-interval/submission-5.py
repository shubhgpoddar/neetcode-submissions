class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)

        res = []

        for i in range(N):
            # start time new > end of interval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

        