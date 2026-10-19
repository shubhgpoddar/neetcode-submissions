class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort(key=lambda x:x[0])

        i = 0
        j = len(nums) - 1

        while (i < j and i < len(nums) and j >= 0):
            a = nums[i][0]
            b = nums[j][0]
            if target > (a + b):
                i = i + 1
            elif target < (a + b):
                j = j - 1
            else:
                res = [nums[i][1], nums[j][1]]
                res.sort()
                return res

        return [-1, -1]


        