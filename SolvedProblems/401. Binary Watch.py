class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        res = []
        
		## number of '1' in bin(m)
        def needed(m):
            if m == 0:
                return 0
            elif m == 1:
                return 1
            elif m %2 ==0:
                return needed(m//2)
            else: #m %2 ==1
                return 1+needed((m-1)//2)
            
        for h in range(12):
            for m in range(60):
                if needed(h) + needed(m) == t:
                    if m < 10:
                        res.append(str(h)+":"+str(0)+str(m))
                    else:
                        res.append(str(h)+":"+str(m))
        return res
