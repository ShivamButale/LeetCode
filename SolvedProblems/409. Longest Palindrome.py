class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        odd = False
        
        for val in counts.values():
            if val%2==0:
                res+=val
            else:
                odd = True
                res += val-1
                
        if odd:
            return res+1
        else:
            return res
        
