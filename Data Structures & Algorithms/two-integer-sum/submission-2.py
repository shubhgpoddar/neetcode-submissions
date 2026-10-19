class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, j in enumerate(nums):
            if target - j in res:
                return [res[target-j], i]
            else:
                res[j] = i
        return []


        