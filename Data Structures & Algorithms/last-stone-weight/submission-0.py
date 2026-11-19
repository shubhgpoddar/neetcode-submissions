class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        10:27
        '''
        heap = []

        for i, stone in enumerate(stones):
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 < stone2:
                new = stone2-stone1
                heapq.heappush(heap,-new)
            elif stone1 > stone2:
                new = stone1-stone2
                heapq.heappush(heap,-new)
        if not heap:
            return 0
        return -heap[0]