class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0]))

        occupied = []

        for start,end in intervals:
            if not occupied or start >= -occupied[0]:
                heapq.heappush(occupied, -end)
            elif -occupied[0] >= end:
                # overlapped
                heapq.heappop(occupied)
                heapq.heappush(occupied, -end)
        return len(intervals) - len(occupied)



        