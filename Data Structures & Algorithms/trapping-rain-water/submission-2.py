class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        N = len(height)

        res = [0]*N
        l = 0
        r = N-1

        while l < N and r > 0 and l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL <= maxR:
                water = min(maxL, maxR) - height[l]
                res[l] = 0 if water < 0 else water
                l+=1
            else:
                water = min(maxL, maxR) - height[r]
                res[r] = 0 if water < 0 else water
                r-=1
        totalWater = sum(res)
        return totalWater
                