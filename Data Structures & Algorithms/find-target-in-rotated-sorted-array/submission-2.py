class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1

        while L <= R:
            k = (L+R)//2

            if nums[k]==target:
                return k
            
            if nums[k] >= nums[L]:
                if target > nums[k] or target < nums[L]:
                    L = k+1
                else:
                    R = k-1
            else:
                # 5 6 7 8 1 2 3
                if target < nums[k] or target > nums[R]:
                    R = k-1
                else: L = k+1


        return -1


        