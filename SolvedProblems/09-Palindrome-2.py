class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x==0):
            return True
        # a = [int(i) for i in str(x)]
        a = list(map(int, str(x)))
        a.reverse()
        a = int("".join(map(str, a)))
        if a==x:
            return True
        return False
