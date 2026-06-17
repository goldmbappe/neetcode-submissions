class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        max_profit = 0
        
        for i in prices:
            if i < minPrice:
                minPrice = i

            profit = i - minPrice
            if profit > max_profit:
                max_profit=profit
        return max_profit
            
                
        