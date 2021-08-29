observed_vals = []
class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        curr_str = str(n)
        val = 0
        
        for i in curr_str:
            val += int(i)*int(i)
         
        if val == 1:
            return True
        
        if val in observed_vals:
            return False
        
        observed_vals.append(val)
        
        return self.isHappy(val)
