class Solution:
    def addDigits(self, num: int) -> int:
        summ = 0
        for i in str(num):
            summ += int(i)
        
        def fun(num):
            curr = 0
            for i in str(num):
                curr += int(i)
            return curr

        while(1):
            if(summ<10):
                return summ
            else:
                summ = fun(summ)
