class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num += (2**32)
        
        final = ""
        hexx = "0123456789abcdef"
        while num>0:
            final = hexx[num%16] + final
            num = num//16
        return final
