class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        curr = 1
        while(n >= curr):
            if n==curr:
                return True 
            curr = curr*4 
        return False
