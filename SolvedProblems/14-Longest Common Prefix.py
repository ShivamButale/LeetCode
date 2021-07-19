class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        cmp = ""
        flag = True 
        first = strs[0]
        
        for i in first:
            #Breakout condition
            if flag == False:
                break
            
            #Successful prefix of previous iteration 
            final = cmp
            
            #Current prefix to compare
            cmp = cmp + i
            
            #check with all other strings 
            for j in range(1, len(strs)):
                
                if cmp != strs[j][0:len(cmp)]:
                    #if cmp not in strs[j]:
                    flag = False
                    break
            
        if(flag == True):
            final = cmp 
        return final
                
        
