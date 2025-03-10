class Solution:
    def rob(self, nums: List[int]) -> int:
        # At every house, u take decisoin. Whether u want to include it and the sum till previosu of previous  OR ignore the current and instead choose sum till the previous 

        prev1 =  0
        prev2 = 0

        for house in nums:
            temp = max(prev1 + house, prev2)
            prev1 = prev2
            prev2 = temp
        
        return temp
