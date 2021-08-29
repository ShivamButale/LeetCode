class Solution:
    def isHappy(self, n: int) -> bool:
        m = 0
        c = set()
        while n != 1:
            c.add(n)
            for a in str(n):
                n = int(a) * int(a) + m
                m = n
            if n in c:
                return False
            m = 0
        return True
