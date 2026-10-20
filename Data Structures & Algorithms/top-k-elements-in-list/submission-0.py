class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num]+=1
        
        frequencyList = []
        for i in frequency:
            frequencyList.append([-frequency[i], i])
        heapq.heapify(frequencyList)

        res = []
        for j in range(k):
            res.append(heapq.heappop(frequencyList)[1])
        return res




        