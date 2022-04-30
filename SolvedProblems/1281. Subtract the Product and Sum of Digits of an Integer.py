class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        
        prod = 1
        total = 0
        
        for i in range(0, len(s)):
            prod *= int(s[i])
            total += int(s[i])    
        
        return prod - total
