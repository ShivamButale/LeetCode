class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        a = 1
        while n>=a:
            if n==a:
                return True 
            a = a*3
        return False
