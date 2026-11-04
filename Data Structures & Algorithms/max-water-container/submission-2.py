class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        7:43
        output: max water = (j-i) * min(heights[i], heights[j])
        Algorithm:
        i = 0 and j = N

        Test case: [2,2,2]
        vol = 4

        '''

        i = 0
        N = len(heights)
        j = N-1

        maxVolume = -float('inf')

        while(i < N and j >=0 and i < j):
            volume = (j-i)*min(heights[i], heights[j])
            maxVolume = max(maxVolume, volume)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxVolume

        