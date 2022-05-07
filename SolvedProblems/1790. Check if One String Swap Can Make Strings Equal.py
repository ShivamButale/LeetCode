class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        ctr = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                ctr +=1
        return ctr <= 2
        
        
