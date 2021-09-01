from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = dict()
        
        i = 0
        j = 0
        
        for i in range(0, len(s)):
            curr_s = s[i]
            curr_t = t[j]
            
            try:                
                if curr_t != mapper[curr_s]:
                    return False
                j+=1
                continue
            except:
                #New entry
                if curr_t in mapper.values():
                    return False
                mapper[curr_s] = curr_t
                j+=1
        
        return True 
