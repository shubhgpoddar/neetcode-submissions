class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        7:56
        default profit: 0
        Algorithm:
        i and j pointers:
        profit = prices[j] - prices[i]
        if profit < 0: i+=1 and j+=1
        if profit > 0: calculate new profit.
        Keep incrementing j pointer until we encounter negative profit.
        i = j and j + 1 because we want the next lowest day to buy

        e.g [10,8,7,5,2]
        0,1 profit < 0
        1,2 profit < 0
        2,3 < 0
        3,4 < 0 return 0

        e.g [10,1,5,6,7,1]
        0,1 profit <0
        1,2 profit = 4
        1,3 pr=5
        1,4 pr=6
        1,1 0 profit and out of bounds
        '''
        i = 0
        N = len(prices)
        j = i + 1

        profit = 0
        while(i < N and j < N and i < j):
            current = prices[j] - prices[i]
            if current > 0:
                profit = max(profit, current)
                j+=1
            else:
                i=j
                j+=1
            
        return profit
        