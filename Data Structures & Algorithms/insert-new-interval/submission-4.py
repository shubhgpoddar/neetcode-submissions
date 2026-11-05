class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        11/4 9:17
        - Already sorted

        Algorithm:
        1. Since intervals are sorted, insert at a position where previous interval's start time is lesser than or equal to current start time and it's lesser than the next interval's start time.
        e.g [[1,3],[5,7]] [2,6]

        res = [[1,7]] 
    
        '''
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        N = len(intervals)
        res = [intervals[0]]
        i = 1

        while i < N:
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i+=1
        return res
        