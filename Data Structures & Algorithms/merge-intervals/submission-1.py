class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        if not intervals:
            return []

        res = []
        res.append(intervals[0])

        j = 1
        while(j < len(intervals)):
            if res[-1][1] >= intervals[j][0]:
                res[-1][1] = max(res[-1][1], intervals[j][1])
            else:
                res.append(intervals[j])
            j+=1

        return res