class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0
        for num in nums:
            currentLength = 0
            prev = num - 1
            if prev not in numSet:
                nextNumber = num
                while nextNumber in numSet:
                    currentLength+=1
                    nextNumber+=1
                longest = max(longest, currentLength)
        return longest










        