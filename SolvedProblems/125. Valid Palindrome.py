class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalnum():
                pass
            else:
                s = s.replace(i,'')
        s = s.lower()
        if s == s[::-1]:
            return True 
        return False
        
