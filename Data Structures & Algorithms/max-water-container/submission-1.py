class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0

        i = 0
        j = n - 1

        while (i < n-1 and j >=0 and i < j):
            current = (j-i)*min(heights[j],heights[i])
            area = max(current, area)

            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1

        return area