class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x==0):
            return True
        num = x
        list1 = []
        while(x):
            list1.append(x%10)
            x = x//10
        y = int("".join(map(str, list1)))
        if y==num:
            return True
        return False
