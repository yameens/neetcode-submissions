class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## looking for the lowest and the highest that follows 
        ## future date that is greater than the minimum
        ## sliding window

        maxProfit = 0
        minimum = float('inf')

        for price in prices: 
            if price < minimum: 
                minimum = price ## the minimum we have seen so far 
            elif price - minimum > maxProfit: 
                maxProfit = price - minimum
        return maxProfit

            


        