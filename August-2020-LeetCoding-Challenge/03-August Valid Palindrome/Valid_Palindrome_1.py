class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        s = s.lower()  #To remove case concerns
        l = []
        s1 = []
        for i in s:
            if i.isalnum():
                l.append(i)
                s1.append(i)
        l.reverse()
        if(l==s1):
            return True 
        else :
            return False
