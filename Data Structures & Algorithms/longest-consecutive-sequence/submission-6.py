class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        8:59
        for each num check if it's the start. 
        - if not start continue to next num
        - if start, increment the num and check in set, record the len of sequence.
        - if res = max(res, len(sequence))
        '''
        nums_set = set(nums)
        i = 0
        N = len(nums)
        res = 0

        while i < N:
            # check if sequence start
            if nums[i] - 1 not in nums_set:
                count = nums[i]
                subsequenceLen = 0
                while count in nums_set:
                    subsequenceLen+=1
                    count+=1
                res = max(res, subsequenceLen)
            i+=1
        return res
            
            
        