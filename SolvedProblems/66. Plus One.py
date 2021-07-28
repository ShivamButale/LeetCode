class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits)))
        n+=1
        l=[]
        while(n):
            l.append(n % 10)
            n = n//10
        l.reverse()
        return l
      
