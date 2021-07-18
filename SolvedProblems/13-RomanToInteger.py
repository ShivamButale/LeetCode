class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        if len(s)==1:
            return d[s]
        for i in range(0, len(s)):
            if s[i]=='I':
                temp = 1
                if i<len(s)-1:
                    if (s[i+1]=="V" or s[i+1]=="X"):
                        temp = -1
                val += temp
            else: 
                if s[i]=='X':
                    temp = 10
                    if i<len(s)-1:
                        if (s[i+1]=="L" or s[i+1]=="C"):
                            temp = -10
                    val += temp
                else: 
                    if s[i]=='C':
                        temp = 100
                        if i<len(s)-1:
                            if (s[i+1]=="D" or s[i+1]=="M"):
                                temp = -100
                        val+=temp
                    else:
                        val+=d[s[i]]
        return val
