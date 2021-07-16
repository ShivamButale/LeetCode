class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        #Negative
        if x<0:
            flag = -1
            x = str(x)[1:]
        y = list(map(int, str(x)))
        y.reverse()
        num = int("".join(map(str, y)))
        if num<-2**31 or num>2**31-1:
            return 0
        return num*flag
