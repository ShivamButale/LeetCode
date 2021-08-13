class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        max_p = 0
        b_price = 2**31-1
        for i in range(0, len(prices)):
            if prices[i] < b_price:
                b_price = prices[i]
            elif prices[i] > b_price:
                if prices[i]-b_price > max_p:
                    max_p = prices[i]-b_price
        return max_p
