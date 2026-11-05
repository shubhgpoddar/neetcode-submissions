class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        11/4 8:59
        Algorithms:
        Intervals can come in any order
        1. Sort by the start intervals
        2. Intervals can be merged if the start index of the interval is less than the end index of the nextprevious interval
        e.g [[1,3],[1,5],[6,7]]
        res = [[1,3]]
        '''
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        i = 1
        N = len(intervals)

        while i < N:
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i+=1
        return res

        
        