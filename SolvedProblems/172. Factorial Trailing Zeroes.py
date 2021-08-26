class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def factorial(n):
            if n==0:
                return 1 
            return n*factorial(n-1)
        
        z = str(factorial(n))
        ctr = 0
        for i in range(len(z)-1, -1, -1):
            if z[i] != '0':
                return ctr
            ctr+=1
