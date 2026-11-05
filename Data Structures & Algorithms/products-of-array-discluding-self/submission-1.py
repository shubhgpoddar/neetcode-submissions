class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        10:46
        Algorithm: O(n)
        [1,2,4,6] - computation - 
        pre [1 1 2 8]
        suf [48 24 6 1]
        

        Output:[product[i+1:] ... ]

        '''
        N = len(nums)
        prefix = [1]*N
        i = 1
        while i < N:
            prefix[i] = nums[i-1]*prefix[i-1]
            i+=1
        
        suffix = [1]*N
        j = N-2
        while j >=0:
            suffix[j] = suffix[j+1]*nums[j+1]
            j-=1
        
        res = []
        for i in range(N):
            res.append(prefix[i]*suffix[i])
        return res

            


        