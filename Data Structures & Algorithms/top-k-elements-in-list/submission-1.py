from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequencyList = [[-counter, element] for element, counter in frequency.items()]

        frequencyList.sort(key=lambda x:x[0])

        res = []

        for i in range(k):
            res.append(frequencyList[i][1])

        return res

        
        