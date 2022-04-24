class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = high-low
        ctr = 0
        
        if(l %2 ==0):
            ctr += (l//2)
            if(low%2==1):
                ctr+=1
        else:
            ctr = (((l-1)//2) + 1)
        
        return ctr
