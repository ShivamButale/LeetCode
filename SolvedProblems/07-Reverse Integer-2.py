class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        ans = 0
        while(abs_x):
            ans = (10*ans) + abs_x%10
            abs_x = abs_x//10
        if(x<0):
            ans = -ans
        else:
            ans = ans
        if ans > 2**31-1 or ans <-2**31:
            return 0
        return ans
            
