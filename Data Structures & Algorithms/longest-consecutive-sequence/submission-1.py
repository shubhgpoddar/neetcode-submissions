class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]
        # [0,1,1,2,3,4,5,6]
        # [2,3,4,4,5,10,20]

        if not nums:
            return 0

        maxlength = 1
        nums.sort()
        current_max = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] == 1:
                current_max+=1
                maxlength = max(maxlength, current_max)
            else:
                current_max = 1
        maxlength = max(maxlength, current_max)
        return maxlength


        