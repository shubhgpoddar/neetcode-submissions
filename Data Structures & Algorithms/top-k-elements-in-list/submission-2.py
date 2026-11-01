class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyMap = defaultdict(int)
        for num in nums:
            frequencyMap[num]+=1

        heap = []
        for num, freq in frequencyMap.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res


        