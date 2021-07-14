class Solution:
    def reverse(self, x: int) -> int:
        x1 = str(x)
        val = 0
        flag = 1
        if(x<0):
            flag=-1
            x1 = x1[1:]
        for i in range(0, len(x1)):
            val += (int(x1[i])*(10**i))
        ans = val*flag
        if(ans > 2**31 -1) or (ans< -1*(2**31)):
            return 0
        return ans
