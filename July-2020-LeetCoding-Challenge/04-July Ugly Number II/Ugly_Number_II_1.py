class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = 0
        i3 = 0
        i5 = 0
        next_2 = 2
        next_3 = 3
        next_5 = 5
        next_ugly = 1
        ugly = [0]
        ugly[0]=1

        if n < len(ugly):
            return ugly[n-1]
        else:
            for x in range(len(ugly), n):
                ugly.append(min(next_2, next_3, next_5))
                if ugly[x]==next_2:
                    i2 += 1
                    next_2 = ugly[i2] * 2

                if ugly[x]==next_3:
                    i3 += 1
                    next_3 = ugly[i3] * 3

                if ugly[x]==next_5:
                    i5=i5+1
                    next_5 = ugly[i5] * 5

            return ugly[-1] 
