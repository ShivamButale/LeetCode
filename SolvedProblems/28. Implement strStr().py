class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        if haystack is None or haystack == "":
            return -1
        
        h = len(haystack)
      
        #Length of needle
        n = len(needle)
        
        if n > h:
            return -1
        
        for i in range(0, h-n+1):
            if needle == haystack[i:i+n]:
                return i
            
        return -1
        
