class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyStock, sellStock = prices[0], 0
        for i in range(1, len(prices)):
            buyStock = min(prices[i], buyStock)
            sellStock = max(sellStock, (prices[i]-buyStock))
        
        return sellStock;