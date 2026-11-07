class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        N = len(nums)
        for i in range(1, N):
            prefix.append(prefix[-1]*nums[i-1])

        suffix = [1]*N
        for i in range(N-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        res = []
        for i in range(N):
            res.append(prefix[i]*suffix[i])
        return res
        