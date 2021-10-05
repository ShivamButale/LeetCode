class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        
        if len(s)==0:
            return True
        
        flag = 0
        
        while(i<len(s) and j<len(t)):
            if s[i] == t[j]:
                flag=1
                i+=1
                j+=1
                continue
            else:
                flag=0
                j +=1
        
        if flag==1 and i==len(s):
            return True
        return False
