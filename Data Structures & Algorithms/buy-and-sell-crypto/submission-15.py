class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices) - 1
        l = 0
        r = 0
        maxProfit = 0

        while r < N:
            r += 1
            if prices[l] >= prices[r]:
                l = r
            else:
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
         
        return maxProfit