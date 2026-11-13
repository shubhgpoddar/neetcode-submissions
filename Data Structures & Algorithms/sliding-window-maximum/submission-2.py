class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        N = len(nums)
        output = []
        l = 0
        r = 0

        while r < N:
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)

            if l > d[0]:
                d.popleft()
            
            if (r + 1) >=k:
                output.append(nums[d[0]])
                l+=1
            r+=1
        return output


        