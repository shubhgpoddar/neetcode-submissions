class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        11/3
        Output = [i,j]
        sort array
        2 pointers. i = 0, j = len(nums) - 1
        if sum > target: j = j-1
        elif sum < target: i = i + 1
        else: return sorted(output)

        Edge cases: [2,3,3,4,5,6] target
        Time complexity: O(nlogn)
        Space: O(1)
        '''

        for i, num in enumerate(nums):
            nums[i] = (num,i)

        nums.sort(key=lambda x:x[0])

        i = 0
        N = len(nums)
        j = N - 1

        while(i < N and j > 0 and i < j):
            total = nums[i][0] + nums[j][0]
            if total > target:
                j-=1
            elif total < target:
                i+=1
            else:
                return [min(nums[i][1], nums[j][1]), max(nums[i][1], nums[j][1])]
        return []
        
        