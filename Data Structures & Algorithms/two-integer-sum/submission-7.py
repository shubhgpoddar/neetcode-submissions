class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Build map of each element tracking the index.
        for each num, if target - num in hashmap and indexes are not the same, return index.
        caveats:
        - any element could appear multiple time in different positions.
        Edge case: [3,3,3,6] target = 6 : 
        False -> You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

        # {4:[0], 5:[1], 6:[2]}  target 10
        '''

        indexMap = {}
        for i, num in enumerate(nums):
            expected = target - num
            if expected in indexMap:
                return [min(i, indexMap[expected]), max(i, indexMap[expected])]
            indexMap[num] = i

        return []