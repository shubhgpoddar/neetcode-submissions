class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        res = max(piles)

        L = 1
        R = max(piles)

        while L<=R:
            mid = (L+R)//2
            hours = 0
            for bananas in piles:
                hours+=math.ceil(bananas/mid)
            if hours > h:
                L = mid + 1
            else:
                res = min(res, mid)
                R = mid - 1
        
        return res

        