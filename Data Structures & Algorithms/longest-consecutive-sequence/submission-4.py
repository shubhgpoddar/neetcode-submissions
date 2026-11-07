class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        10 min - not optimal
        No sorting allowed
        hashset of elements - unique elements and O(1) look up: O(N)
        - for each element increment 1 until we cant find the element in hashset
        record max subseseuqnce found
        repeat for every element

        Time limit exceeded ~

        optimizations:
        - instead of every number see if that number was a start
        '''
        N = len(nums)
        nums_set = set(nums)
        maxLength = 0
        for num in nums:
            if num - 1 not in nums_set:
                count = num
                subsequence_length = 0
                while count in nums_set:
                    subsequence_length+=1
                    count+=1
                maxLength = max(maxLength, subsequence_length)
                if maxLength == N:
                    return maxLength
        return maxLength

        