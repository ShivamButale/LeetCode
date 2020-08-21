class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0:
            return 0
        initial_n = n
        l = 0
        while(n):
            if n<l:
                break
            else:
                n = n-l
                l = l+1
        return l-1
