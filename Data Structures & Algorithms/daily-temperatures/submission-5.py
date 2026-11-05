class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        5:55
        Algorithm:
        1. Add the temperature with index to a min heap
        2. When we encounter a temperature, peak in the heap and check if it's a warmer day (temp - heap[0]). 
            pop until we no longer have warmer days in the heap
        For remaining heap items: no warmer days
        e.g [30,38,30,36,35,40,28]
        heap: (40,5)

        res = [1 4 1 2 1 0 0]

        '''
        N = len(temperatures)
        res = [0]*N
        heap = []

        for index, temp in enumerate(temperatures):
            while(heap and temp > heap[0][0]):
                t, i = heapq.heappop(heap)
                res[i] = index - i
            heapq.heappush(heap, (temp, index))
        return res
