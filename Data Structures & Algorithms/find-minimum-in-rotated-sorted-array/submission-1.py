class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1:43
        - k times (0, n-1) = 0,5 k = 2
        (L,R) (0,5) k=2 numK=5 
            compare with first. if greater, move right L = mid+1
            if smaller, move left R = mid - 1
        (L,R) (3,5) k = 4 numK = 1
        (3,3) k = 3 numK = 6
        (4,3) out of bounds

        (L,R)(0,5) K = 2 val = 0
        (0,1) K = 0 val = 4
        (0,-1) out of bounds
        '''
        N = len(nums)
        L = 0
        R = N-1
        res = float('inf')

        while L<=R:
            k = (L+R)//2
            if nums[k] > nums[-1]:
                L = k+1
            else:
                R = k-1
            res = min(res, nums[k])
        return res