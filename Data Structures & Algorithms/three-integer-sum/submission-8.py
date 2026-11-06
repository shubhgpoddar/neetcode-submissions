class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        no duplicate triplets => hashset()
        freq map = {-4:1, -1:2, 0:1, 1:1, 2:2}
        # [-4,-1,-1,0,1,2]
        -4 : target = 4 if target > nums[j] + nums[k] increment j else decrement k
        j = i+1 and k = len(array)
        '''
        nums.sort()
        res = set()
        N = len(nums)
        seen = set()

        for i in range(N):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            target = -nums[i]
            j = i+1
            k = N-1
            while j < N and j < k:
                if nums[j]+nums[k] == target:
                    op = (nums[i], nums[j], nums[k])
                    res.add(op)
                    j+=1
                    k-=1
                elif target>nums[j]+nums[k]:
                    j+=1
                else:
                    k-=1
        output = []
        for el in res:
            output.append(list(el))
        return output