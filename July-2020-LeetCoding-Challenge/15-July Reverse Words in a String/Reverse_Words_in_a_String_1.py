class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip()
        if len(s)==0:
            return ""
        #print("s = ", s)
        l = s.split(" ")
        #print("l = ", l)
        ok=[]
        for i in l:
            if len(i)  !=0:
                ok.append(i)
        l = []
        for i in ok:
            l.append(i)
        #print("after remove l = ", l)
        l.reverse()
        #print("reversed l = ", l)
        str1 = ""
        for i in range(0, len(l)-1):
            str1 += l[i]
            str1 += " "
        str1 += l[-1]
        
        return str1
