class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## buy low sell high 

        maxProfit = 0
        lowest = float("inf")
        for price in prices: 
            if price < lowest: 
                lowest = price
            if price - lowest > maxProfit: 
                maxProfit = price - lowest
            
        
        return maxProfit


        