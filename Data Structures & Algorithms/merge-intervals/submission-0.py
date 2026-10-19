class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])

        output = [intervals[0]]

        for i, j in intervals:
            if output[-1][1] >= i:
                output[-1][1] = max(output[-1][1], j)
            
            else:
                output.append([i, j])
        return output
        