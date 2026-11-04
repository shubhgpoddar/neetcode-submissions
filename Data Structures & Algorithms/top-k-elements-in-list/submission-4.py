class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        12:27 - 12:32
        Algorithm:
        1. Put elements with [frequency, element] in a heap
        2. If size of heap exceeds k, pop
        3. Return the elements

        nums = [1,2,2,3,3,3], k = 2
        {1:1, 2:2, 3:3}
        heap = [[2,2],[3,3]]
        '''
        freq = defaultdict(int)

        for num in nums:
            freq[num]+=1
        
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            element = heapq.heappop(heap)
            res.append(element[1])
        
        return res
        