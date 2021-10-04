class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        for i in t:
            if i not in d:
                return i
            d[i] -= 1
            
        for i in d:
            if d[i]!=0:
                return i
