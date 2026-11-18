class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        9:10
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        for each num run 2 pointers i and j
        (-4 -1 2) = -3 j out of bounds
        (-1 -1 2) = 0 triplet
        -1 in seen - dont record
         (0)
        '''

        nums.sort()
        N = len(nums)
        res = set()
        

        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = N-1
            target = -nums[i]
            while j < N and j < k:
                if nums[j] + nums[k] == target:
                    output = (nums[i], nums[j], nums[k])
                    res.add(output)
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    j+=1
        result = []
        for op in res:
            result.append(list(op))
        return result



        