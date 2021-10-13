class Solution:
    def countSegments(self, s: str) -> int:
        if(s==""):
            return 0
        s= s.lstrip(' ')
        s= s.rstrip(' ')
        ctr = 0 
        flag = 0
        for i in s:
            #Non-blank
            if i!=' ':
                if flag==0:
                    flag=1
                    ctr += 1
            else:
                flag=0
        return ctr
