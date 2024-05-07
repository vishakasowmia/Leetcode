class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for sell in prices[1:]:
            current_profit = sell - buy
            if sell < buy:
                 buy = sell
            elif profit < current_profit:
                profit = current_profit
        return profit
                
              
            
        
        