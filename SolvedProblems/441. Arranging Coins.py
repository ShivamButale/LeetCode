class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr_req = 1
        ctr = 0
        while(n):
            if n<curr_req:
                break
            elif n==curr_req:
                return ctr+1
            else:
                ctr += 1  
                n -= curr_req
                curr_req += 1
        return ctr
        
