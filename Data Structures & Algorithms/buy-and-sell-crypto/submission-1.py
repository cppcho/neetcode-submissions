class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        smallest = prices[l]
        for r in range(len(prices)):
            if prices[r] < smallest:
                l = r
                smallest = prices[r]
            res = max(prices[r] - prices[l], res)
        
        return res
        