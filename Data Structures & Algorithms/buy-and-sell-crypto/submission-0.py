class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxProfit = 0

        for R in range(len(prices)):
            curr = prices[R] - prices[L]
            if curr < 0:
                L=R
            maxProfit = max(maxProfit, curr)
        return maxProfit
        